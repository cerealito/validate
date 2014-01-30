__author__ = 'saflores'

class VarComparator:
    def __init__(self):
        print ('comparator constructor')

    def compare(self, var1, var2):

        error = 0

        # TODO: this should not stop in length but in actual sampling times.
        if len(var1.times) != len(var2.times):
            raise ValueError ('Variables must have equal domains')

        for t in var1.times:
            if var1.value_at(t) != var2.value_at(t):
                print ('error')




