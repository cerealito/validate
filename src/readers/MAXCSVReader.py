from _hashlib import new
import builtins

__author__ = 'saflores'

import csv
from Variable import Variable

csv.register_dialect('MAX', delimiter=';', skipinitialspace=True)

class MAXCSVReader:
    def __init__(self, csv_f):
        """
        A Max produced CSV file has the following shit:
        """

        self.variables = []
        self.times = []
        self.read(csv_f)

    def read(self, f):

        with open(f) as csv_f:
            # TODO: test for correct file type with libmagic or similar.
            # relying on readline() will fail with a very large file with no new lines

            # check that there is a header:
            l = csv_f.readline()
            if l.strip() != '#HEADER':
                raise TypeError('Format not supported')



            generic_reader = csv.reader(csv_f, dialect='MAX')

            #########################################################
            # skip everithing until finding 'DATA'
            while l != '#DATA\n':
                l = csv_f.readline()

            #########################################################
            # check that we will read the stuff in the right order
            l = csv_f.readline()
            if l != 'Name;Type;FirstDim;SndDim;LocalAttributes\n':
                raise TypeError('Format not supported')

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

            #########################################################
            # start reading the payload and populate each variable
            for row in generic_reader:
                if row[0] == '#END':
                    break
                # Times are kept as floats so that we can search easily among
                # different formats
                t = float(row[time_column_idx])

                # keep track of the times:
                self.times.append(float(t))

                for v in self.variables:
                    #print('\tvar ' + v.name + '=', row[v.index])
                    v.samples[float(t)] = row[v.index]
                    #v.times.append(t)
                    #v.values.append(row[v.index])

    def get_variable(self, fullname):
        look_up_v = Variable(fullname)

        if look_up_v in self.variables:
            idx = self.variables.index(look_up_v)
            return self.variables[idx]
        else:
            import sys
            sys.stdout.flush()
            sys.stderr.write('Variable ' + fullname + ' was not read in the csv file\n')
            sys.stderr.write('Returning None\n')
