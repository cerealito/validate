import unittest

from src.readers.MAXCSVReader import MAXCSVReader

__author__ = 'saflores'

class MAXCSVReader_tester(unittest.TestCase):

    def test_read(self):
        print ('hello...')

        r = MAXCSVReader('../00_install/ref_214.csv')

        for v in r.variables:
            print(v)
        print()
        myVar = r.get_variable('CPC_SACU\SACU_p_delta_sensor_out_psid')

        for t in myVar.times:
            print('{:03.8f} '.format(t), myVar.value_at(t))

if __name__ == '__main__':
    unittest.main()