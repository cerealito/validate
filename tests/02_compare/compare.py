import unittest
from src.FileComparator import FileComparator, RSummary

__author__ = 'saflores'

class FileComparator_tester(unittest.TestCase):

    def test_mini(self):
        print('Comparing to a mini error...')
        t = '../00_install/small.csv'
        r = '../00_install/small_2.csv'

        fc = FileComparator(t, r)
        res = fc.compare()

        print('\n### Overall result is: ', res.files_are_equal)
        self.assertFalse(res.files_are_equal)

    def test_equals(self):
        print('comparing a file to itself')
        fp = '../00_install/test_214.csv'

        fc = FileComparator(fp, fp)
        res = fc.compare()

        print('\n### Overall result is: ', res.files_are_equal)
        self.assertTrue(res.files_are_equal)

    def test_diff(self):
        print('Comparing to a known error...')
        t = '../00_install/test_214.csv'
        r = '../00_install/ref_214.csv'

        fc = FileComparator(t, r)
        res = fc.compare()

        print('\n### Overall result is: ', res.files_are_equal)
        self.assertFalse(res.files_are_equal)

if __name__ == '__main__':
    unittest.main()