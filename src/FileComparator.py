from VarComparator import VarComparator
from readers.MAXCSVReader import MAXCSVReader

__author__ = 'saflores'


class FileComparator:
    @staticmethod
    def compare(file_test, file_ref):
        all_vars_equal = True
        #TODO: decide what type of file this is
        # for now we only have one reader so...

        record_test = MAXCSVReader(file_test)
        record_ref = MAXCSVReader(file_ref)

        if len(record_test.variables) != len(record_ref.variables):
            raise NotImplementedError ('Files must have the same number of variables')

        if len(record_test.times) != len(record_ref.times):
            raise NotImplementedError('files do not have the same number of samples')

        print('Comparing ' + str(len(record_test.variables)) + ' variables')

        for v_test in record_test.variables:

            v_ref = record_ref.get_variable(v_test.fullname)

            vc = VarComparator()
            result = vc.compare(v_test, v_ref)
            print(v_test.name, '... ', result)

            all_vars_equal = result and all_vars_equal

        return all_vars_equal





