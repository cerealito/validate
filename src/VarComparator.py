__author__ = 'saflores'


class VarComparator:
    def compare(self, test, ref):
        both_are_equal = True
        added_error_percentage = 0

        # TODO: this should not stop in length but in actual sampling times.
        if len(test.times) != len(ref.times):
            raise ValueError('Variables must have equal domains')

        for t in test.times:

            test_v = test.value_at(t)
            ref_v = ref.value_at(t)
            if test_v != ref_v:
                both_are_equal = False
                added_error_percentage += VarComparator.__error_percent__(test_v, ref_v)

        avg_error_percentage = added_error_percentage/len(test.times)

        return both_are_equal, avg_error_percentage


    @staticmethod
    def __error_percent__(test, ref):
        if float(ref) != 0:
            return abs(((float(ref) - float(test))*100)/float(ref))
        else:
            # if a ref sample has a value of zero
            #  100% error if test sample is not zero as well
            return 100 if float(test) else 0
