__author__ = 'cerealito'

class FileCmpResult:
    def __init__(self, file_test, file_ref, is_acceptable, results_l, date):
        self.file_test = file_test
        self.file_ref = file_ref
        self.is_acceptable = is_acceptable
        self.result_l = results_l
        self.date = date

class ResultCouple:
    def __init__(self, test_var, ref_var, match, error):
        self.test_var = test_var
        self.ref_var = ref_var
        self.match = match
        self.error = error

        self.status = 'ko'
        if error <= 5:
            self.status = 'warning'
        if error <= 1:
            self.status = 'passed'
        if error == 0:
            self.status = 'matched'
        if error < 0:
            self.status = 'ko'

    def __str__(self):
        return '{:<60} {:.2f}%  {:<7}'.format(self.test_var.name, self.error, self.status)
