from VarComparator import VarComparator
from readers.MAXCSVReader import MAXCSVReader

__author__ = 'saflores'


class FileComparator:
    def __init__(self, file_test, file_ref):
        self.different_vars = []

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

            vc = VarComparator()

            result, error = vc.compare(v_test, v_ref)
            print(v_test.name, '... ', result, str(error) + '%')

            all_vars_equal = result and all_vars_equal

            if not result:
                self.different_vars.append((v_test, v_ref))

        return all_vars_equal

    def get_different_var_tuples(self):
        return self.different_vars



