import unittest
from src.FileComparator import FileComparator as fc

__author__ = 'saflores'

class FileComparator_tester(unittest.TestCase):

    def test_mini(self):
        print('Comparing to a mini error...')
        t = '../00_install/small.csv'
        r = '../00_install/small_2.csv'

        r = fc.compare(t, r)

        print('\n### Overall result is: ', r)
        self.assertFalse(r)

    def test_equals(self):
        print('comparing a file to itself')
        fp = '../00_install/test_214.csv'
        r = fc.compare(fp, fp)

        print('\n### Overall result is: ', r)
        self.assertTrue(r)

    def test_diff(self):
        print('Comparing to a known error...')
        t = '../00_install/test_214.csv'
        r = '../00_install/ref_214.csv'

        r = fc.compare(t, r)

        print('\n### Overall result is: ', r)
        self.assertFalse(r)

if __name__ == '__main__':
    unittest.main()