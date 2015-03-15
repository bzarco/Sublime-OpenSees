from ..lib.helpers import RunBase


class RunSingleParallel(RunBase):

    def get_name(self):
        return "Single Parallel"

    def is_parallel(self):
        return True

    def get_exe_setting_name(self):
        return "opensees_sp"