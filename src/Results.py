__author__ = 'cerealito'

class FileCmpResult:
    def __init__(self, file_test, file_ref, equal, results_l):
        self.file_test = file_test
        self.file_ref = file_ref
        self.files_are_equal = equal
        self.result_l = results_l

class ResultCouple:
    def __init__(self, test_var, ref_var, match, error):
        self.test_var = test_var
        self.ref_var = ref_var
        self.match = match
        self.error = error

    def __str__(self):
        return '{:<60} {:.2f}%'.format(self.test_var.name, self.error)
