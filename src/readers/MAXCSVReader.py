from _hashlib import new

__author__ = 'saflores'

import csv

csv.register_dialect('MAX', delimiter=';', skipinitialspace=True)


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
        return self.model + ':' + self.name + '  [' + self.type + ']'


class MAXCSVReader:
    def __init__(self, csv_f):
        '''
        A Max produced CSV file has the following shit:
        '''

        self.nbSamples = 0
        self.variables = []

        self.read(csv_f)

    def read(self, f):

        with open(f) as csv_f:
            l = csv_f.readline()

            generic_reader = csv.reader(csv_f, dialect='MAX')

            #########################################################
            # skip everithing until finding 'DATA'
            while l != '#DATA\n':
                l = csv_f.readline()

            #########################################################
            # check that we will read the stuff in the right order
            l = csv_f.readline()
            if l != 'Name;Type;FirstDim;SndDim;LocalAttributes\n':
                print('Format not supported')
                raise TypeError

            #########################################################
            # Create a new variable for each entry in the DATA
            for row in generic_reader:
                if row[0] == '#PAYLOAD':
                    break

                new_var = Variable(row[0], row[1], row[2], row[3])
                self.variables.append(new_var)


            #########################################################
            # start reading the payload and populate each variable
            ## skip the header line:
            ## TODO: maybe can be used for a check?
            h = next(generic_reader)


            i = 0
            for row in generic_reader:

                col = 0;
                t = row[col]
                print(str(len(row)) + '  ' + str(len(self.variables)))




                i += 1
                if i > 10:
                    break