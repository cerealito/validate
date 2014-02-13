from encodings import big5
import unittest
from charts.generation import generate_png
from FileComparator import FileComparator

__author__ = 'saflores'


class GraphTester(unittest.TestCase):
    #################################################################################
    def test_mini(self):
        print('Comparing and graphing a mini error...')
        t = '../00_install/small.csv'
        r = '../00_install/small_2.csv'
        pb_list = []

        fc = FileComparator(t, r)
        res = fc.compare()

        print('\n### Overall result is: ', res.is_acceptable)
        if not res.is_acceptable:
            print('Errors exist (' + str(len(fc.different_vars)) + ')')

        # for every couple of variables, generate a png
        for result in fc.result_couple_l:

            of = generate_png(result.test_var, result.ref_var)
            self.assertIsNotNone(of)

        self.assertFalse(res.is_acceptable)

    #################################################################################
    def test_equals(self):
        print('comparing a file to itself')
        fp = '../00_install/test_214.csv'

        fc = FileComparator(fp, fp)
        res = fc.compare()

        print('\n### Overall result is: ', res.is_acceptable)
        if not res.is_acceptable:
            print('Errors exist (' + str(len(fc.different_vars)) + ')')

        # for every couple of variables, generate a png
        for result in fc.result_couple_l:
            of = generate_png(result.test_var, result.ref_var)
            self.assertIsNotNone(of)

        self.assertTrue(res.is_acceptable)

    #################################################################################
    def test_diff(self):
        print('Comparing to a known error...')
        t = '../00_install/test_214.csv'
        r = '../00_install/ref_214.csv'

        fc = FileComparator(t, r)
        res = fc.compare()

        print('\n### Overall result is: ', res.is_acceptable)
        if not res.is_acceptable:
            print('Errors exist (' + str(len(fc.different_vars)) + ')')

        # for every couple of variables, generate a png
        for result in fc.result_couple_l:
            of = generate_png(result.test_var, result.ref_var)
            self.assertIsNotNone(of)

        self.assertTrue(res.is_acceptable)

if __name__ == '__main__':
    unittest.main()