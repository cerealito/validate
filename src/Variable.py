__author__ = 'saflores'

class Variable:
    def __init__(self, fullname, v_type=None, dim1=0, dim2=0):

        self.fullname = fullname
        self.type = v_type
        self.dim1 = dim1
        self.dim2 = dim2
        self.index = 0

        self.times = []
        self.values = []

        tokens = self.fullname.split('\\')

        self.model = tokens[0]
        self.name = tokens[1]

    def value_at(self, time):
        idx = self.times.index(time)
        return self.values[idx]

    def __str__(self):
        return '{0:2d} '.format(self.index) + '{:<8}'.format(self.type) +\
               '{:<} '.format(len(self.values)) +\
               self.model + ':' + self.name

    def __eq__(self, other):
        if self.fullname == other.fullname:
            return True
        else:
            return False

    def compare_to(self, other):
        both_are_equal = True
        added_error_percentage = 0

        # TODO: this should not stop in length but in actual sampling times.
        if len(self.times) != len(other.times):
            raise ValueError('Variables must have equal domains')

        for t in self.times:
            test_v = self.value_at(t)
            ref_v = other.value_at(t)
            if test_v != ref_v:
                both_are_equal = False
                added_error_percentage += Variable.__error_percent__(test_v, ref_v)

        avg_error_percentage = added_error_percentage/len(self.times)

        return both_are_equal, avg_error_percentage


    @staticmethod
    def __error_percent__(test, ref):
        if float(ref) != 0:
            return abs(((float(ref) - float(test))*100)/float(ref))
        else:
            # if a ref sample has a value of zero
            #  100% error if test sample is not zero as well
            return 100 if float(test) else 0
