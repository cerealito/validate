from readers.MAXCSVReader import MAXCSVReader

__author__ = 'saflores'

import unittest

import numpy as np
import matplotlib.pyplot as plt


class MatplotlibTest(unittest.TestCase):

    def test_plot(self):
        print ('hello...')

        r = MAXCSVReader('ref_214.csv')

        for v in r.variables:
            print(v)
        print()

        myVar = r.get_variable('CPC_SACU\SACU_h_cabin_alt_target_ft_out')

        # o_values = []
        # for t in r.times:
        #     o_values.append(myVar.samples.get(t))

        plt.plot(myVar.times, myVar.values, 'r-.')
        plt.show()


if __name__ == '__main__':
    unittest.main()