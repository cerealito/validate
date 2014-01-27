from _hashlib import new

__author__ = 'saflores'

import csv
from Variable import Variable

csv.register_dialect('MAX', delimiter=';', skipinitialspace=True)




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

                new_var = Variable(fullname=row[0], v_type=row[1], dim1=row[2], dim2=row[3])
                self.variables.append(new_var)

            #########################################################
            ## find every variable created in the step above in the header:
            header = next(generic_reader)
            time_column_idx = 0
            for v in self.variables:
                try:
                    v.index = header.index(v.fullname)
                except ValueError:
                    print('Column not found')
                finally:
                    if v.index == 0:
                        # this means that time is not the very first column in the payload.
                        # screw it we do not handle this kind of format
                        print('Format not supported')
                        raise TypeError

            for v in self.variables:
                print(v)

            #########################################################
            # start reading the payload and populate each variable
            i = 0

            for row in generic_reader:
                t = row[time_column_idx]
                print('analizing t=',t)

                for v in self.variables:
                    print('\tvar ' + v.name + '=', row[v.index])

                    v.samples[t] = row[v.index]

                i += 1
                if i > 10:
                    break

            print( self.variables[3].samples)