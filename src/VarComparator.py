__author__ = 'saflores'

class VarComparator:
    def compare(self, var1, var2):
        both_are_equal = True

        # TODO: this should not stop in length but in actual sampling times.
        if len(var1.times) != len(var2.times):
            raise ValueError('Variables must have equal domains')

        for t in var1.times:
            if var1.value_at(t) != var2.value_at(t):
                both_are_equal=False
                break

        return both_are_equal
