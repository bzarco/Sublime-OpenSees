import sublime, sublime_plugin
import os
import shutil
import re
import Default


class Settings(object):
    @staticmethod
    def get(key):
        os.environ["PackageDir"] = os.path.join(sublime.packages_path(), "OpenSees")
        settings = sublime.load_settings("OpenSees.sublime-settings")
        project_data = sublime.active_window().project_data()
        keys = key.split(".")
        k = keys[0]
        if project_data is not None and k in project_data:
            setting = project_data[k]
        else:
            setting = settings.get(k)
        for k in keys[1:]:
            setting = setting[k]
        return Settings._replace_references(setting)
    @staticmethod
    def _replace_references(setting):
        r_lambda = lambda token: re.compile(r"\${" + token + "}")
        if isinstance(setting, dict):
            for k, v in setting.items():
                setting[k] = Settings._replace_references(v)
        if isinstance(setting, list):
            for i, v in enumerate(setting):
                setting[i] = Settings._replace_references(v)
        if isinstance(setting, str):
            setting = os.path.expandvars(setting)
            for match in r_lambda(r"[^}]*").findall(setting):
                token = match[2:-1]
                setting = r_lambda(token).sub(str(Settings.get(token)).replace("\\", "\\\\"), setting)
        return setting

def norm_path(path):
    return os.path.normpath(os.path.normcase(path))

def save_all_views(window, path):
    for view in window.views():
        fname = view.file_name()
        if (fname and view.is_dirty() and os.path.exists(fname) and norm_path(fname).startswith(norm_path(path))):
            view.run_command("save")

def cpu_count():
    # Linux, Unix and MacOS:
    if hasattr(os, "sysconf"):
        if os.sysconf_names.has_key("SC_NPROCESSORS_ONLN"):
            ncpus = os.sysconf("SC_NPROCESSORS_ONLN")
            if isinstance(ncpus, int) and ncpus > 0:
                return ncpus
        else:
            return int(os.popen2("sysctl -n hw.ncpu")[1].read())
    # Windows:
    if os.environ.has_key("NUMBER_OF_PROCESSORS"):
        ncpus = int(os.environ["NUMBER_OF_PROCESSORS"]);
        if ncpus > 0:
            return ncpus
    return 1 # Default

class OnDoneExecCommand(Default.exec.ExecCommand):
    # overriden from ExecCommand
    def __init__(self, window, display_name=None, on_done=None, stdout=None):
        super().__init__(window)
        self.display_name = display_name
        self.on_done = on_done
        self.stdout = stdout
    # overriden from ExecCommand
    def run(self, **kwargs):
        super().run(**kwargs)
        self.append_string(self.proc, "[%s Started]\n\n" % self.display_name)
    # overriden from ExecCommand
    def append_string(self, proc, str):
        if not proc.poll() and self.display_name:
            str = "\n\n" + re.sub(r"(Finished)", self.display_name + r" \1", str, 1)
        super().append_string(proc, str)
        if isinstance(self.stdout, list):
            self.stdout.append(str)
    # overriden from ExecCommand
    def finish(self, proc):
        super().finish(proc)
        sublime.set_timeout(self.run_callbacks, 0)
    # custom method
    def popen(self):
        return self.proc.proc
    # custom method
    def run_message(self, message):
        self.run(shell_cmd = ":: [%s] %s" % (self.display_name, message))
        self.append_string(self.proc, message)
    # custom method
    def run_callbacks(self):
        if not isinstance(self.on_done, list):
            self.on_done = [self.on_done]
        for od in self.on_done:
            if od is not None:
                od()

class RunBase(sublime_plugin.WindowCommand):
    def run(self, paths = []):
        name = "OpenSees " + self.get_name()
        path = self.get_path(paths)
        basename = os.path.basename(path)
        command = OnDoneExecCommand(self.window, "RUN %s for \"%s\"" % (name, basename))
        if path is None:
            command.run_message("Input file \"%s\" is not a valid %s file." % (path, name))
            return None
        save_all_views(self.window, path)
        cmd = self.get_cmd(name, basename, command)
        if cmd is None:
            return None
        command.run(
            shell_cmd = cmd,
            file_regex = r"^\s*\(file \"([^\"]+)\" line (\d+)\)$",
            working_dir = os.path.dirname(path)
        )
        return command.popen()
    def is_enabled(self, paths = []):
        return self.get_path(paths) is not None
    def is_visible(self, paths = []):
        return self.is_enabled(paths)
    def get_path(self, paths):
        path = None
        if len(paths) < 1:
            path = self.window.active_view().file_name()
        elif len(paths) == 1:
            path = paths[0]
        if (path is None or not os.path.exists(path)):
            return None
        return path
    def get_cmd(self, name, basename, command):
        executable = Settings.get(self.get_exe_setting_name())
        if shutil.which(executable) is None:
            command.run_message("%s executable \"%s\" was not found, make sure it is installed." % (name, executable))
            return None
        cmd = "%s %s" % (executable, basename)
        if self.is_parallel():
            mpiexec = Settings.get("mpiexec")
            if shutil.which(mpiexec) is None:
                command.run_message("MPI executable for %s \"%s\" was not found, make sure it is installed." % (name, mpiexec))
                return None
            max_processor_count = cpu_count()
            try:
                processor_count = int(Settings.get("processor_count"))
                if not 0 < x <= max_processor_count:
                    raise Exception("Processor count not in valid range")
            except Exception:
                processor_count = max_processor_count
            cmd = "%s -np %s " % (mpiexec, processor_count) + cmd
        return cmd
    def get_name(self):
        raise NotImplementedError("Should have implemented \"get_name(self)\" method.")
    def is_parallel(self):
        raise NotImplementedError("Should have implemented \"is_parallel(self)\" method.")
    def get_exe_setting_name(self):
        raise NotImplementedError("Should have implemented \"get_exe_setting_name(self)\" method.")