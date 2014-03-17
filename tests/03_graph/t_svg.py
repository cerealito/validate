import unittest
from charts.svg import generate_svg

from FileComparator import FileComparator

__author__ = 'saflores'


class GraphTester(unittest.TestCase):
    def test_mini(self):
        print('Comparing and graphing a mini error...')
        t = '../00_install/small.csv'
        r = '../00_install/small_2.csv'

        fc = FileComparator(t, r)
        res = fc.compare()

        print('\n### Overall result is: ', res.is_acceptable)

        # for every couple of variables, generate a png
        for result in fc.result_couple_l:
            of = generate_svg(result.test_var, result.ref_var, './output')
            self.assertIsNotNone(of)

        self.assertFalse(res.is_acceptable)

    #################################################################################
    def test_diff(self):
        print('Comparing to a known error...')
        t = '../00_install/test_214.csv'
        r = '../00_install/ref_214.csv'

        fc = FileComparator(t, r)
        res = fc.compare()

        print('\n### Overall result is: ', res.is_acceptable)

        # for every couple of variables, generate a png
        for result in fc.result_couple_l:
            of = generate_svg(result.test_var, result.ref_var)
            self.assertIsNotNone(of)

        self.assertTrue(res.is_acceptable)

if __name__ == '__main__':
    unittest.main()