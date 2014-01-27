__author__ = 'saflores'

class Variable:
    def __init__(self, fullname, v_type, dim1, dim2):

        self.fullname = fullname
        self.type = v_type
        self.dim1 = dim1
        self.dim2 = dim2
        self.index = 0
        self.samples = {}

        tokens = self.fullname.split('\\')

        self.model = tokens[0]
        self.name = tokens[1]

    def __str__(self):
        return 'idx: ' + str(self.index) + ' [' + self.type + ']' + self.model + ':' + self.name
