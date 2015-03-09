from ..lib.helpers import RunBase


class RunSequential(RunBase):

    def get_name(self):
        return "Sequential"

    def is_parallel(self):
        return False

    def get_exe_setting_name(self):
        return "opensees"