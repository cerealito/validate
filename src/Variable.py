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
