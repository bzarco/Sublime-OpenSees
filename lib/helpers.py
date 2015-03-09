import sublime
import os
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