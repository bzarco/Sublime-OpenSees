from ..lib.helpers import RunBase


class RunMultipleParallel(RunBase):

    def get_name(self):
        return "Multiple Parallel"

    def is_parallel(self):
        return True

    def get_exe_setting_name(self):
        return "opensees_mp"