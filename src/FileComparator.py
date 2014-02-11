from VarComparator import VarComparator
from readers.MAXCSVReader import MAXCSVReader
from Results import ResultCouple, FileCmpResult
__author__ = 'saflores'


class FileComparator:
    def __init__(self, file_test, file_ref):
        self.file_test = file_test
        self.file_ref = file_ref
        self.different_vars = []
        self.result_couple_l = []

        #TODO: decide what type of file this is
        ###############################################################
        # for now we only have one kind of reader so create two of them
        self.record_test = MAXCSVReader(file_test)
        self.record_ref = MAXCSVReader(file_ref)

        ###############################################################
        # check that the records are actually equivalent:
        if len(self.record_test.variables) != len(self.record_ref.variables):
            raise NotImplementedError('Files must have the same number of variables')

        if len(self.record_test.times) != len(self.record_ref.times):
            raise NotImplementedError('files do not have the same number of samples')

    def compare(self):
        all_vars_equal = True

        ###############################################################
        # some output to the user
        print('Comparing ' + str(len(self.record_test.variables)) + ' variables')

        ###############################################################
        # iterate over the test's variables and compare it with it's
        # reference counterpart
        for v_test in self.record_test.variables:

            v_ref = self.record_ref.get_variable(v_test.fullname)
            # TODO see if you can turn this to a function or static method of class 'Variable'
            vc = VarComparator()
            vars_match, error = vc.compare(v_test, v_ref)

            r = ResultCouple(v_test, v_ref, vars_match, error)
            self.result_couple_l.append(r)
            print(r)

            all_vars_equal = vars_match and all_vars_equal

            if not vars_match:
                self.different_vars.append((v_test, v_ref))

        ###############################################################
        # Pack everything in an object and return
        file_cmp_result = FileCmpResult(self.file_test, self.file_ref, all_vars_equal, self.result_couple_l)

        return file_cmp_result

