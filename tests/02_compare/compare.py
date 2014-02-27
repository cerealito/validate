from queue import Queue, Empty
import unittest
from AsyncFileComparator import AsyncFileComparator

__author__ = 'saflores'

class FileComparator_tester(unittest.TestCase):

    def test_mini(self):
        print('Comparing to a mini error...')
        t = '../00_install/small.csv'
        r = '../00_install/small_2.csv'

        q = Queue()
        fc = AsyncFileComparator(t, r, q)
        fc.start()

        # join blocks the caller thread until fc finishes
        fc.join()
        res = q.get_nowait()

        print('\n### Overall result is: ', res.is_acceptable)
        self.assertFalse(res.is_acceptable)

    def test_equals(self):
        print('comparing a file to itself')
        fp = '../00_install/test_214.csv'

        q = Queue()
        fc = AsyncFileComparator(fp, fp, q)
        fc.start()

        # join blocks the caller thread until fc finishes
        fc.join()
        res = q.get_nowait()

        print('\n### Overall result is: ', res.is_acceptable)
        self.assertTrue(res.is_acceptable)

    def test_diff(self):
        # lists 44 secs
        # od    2.23 secs!
        # dicts
        print('Comparing to a known error... (should pass)')
        t = '../00_install/test_214.csv'
        r = '../00_install/ref_214.csv'

        q = Queue()
        fc = AsyncFileComparator(t, r, q)
        fc.start()

        # join blocks the caller thread until fc finishes
        fc.join()
        res = q.get_nowait()

        print('\n### Overall result is: ', res.is_acceptable)
        self.assertTrue(res.is_acceptable)

if __name__ == '__main__':
    unittest.main()