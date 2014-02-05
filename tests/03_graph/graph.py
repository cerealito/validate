import unittest
from src.FileComparator import FileComparator
import matplotlib.pyplot as plt

__author__ = 'saflores'


class GraphTester(unittest.TestCase):
    @staticmethod
    def generate_png(test, ref):
        plt.plot(ref.times, ref.values, color='#00FF21',
                 label='ref', linestyle='solid', linewidth=2.5)
        plt.plot(test.times, test.values, color='#FF1D00',
                 label='test', linestyle='dashed', linewidth=1.5)
        plt.ylabel(test.name)
        plt.xlabel('seconds')
        plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), fancybox=True, shadow=True)

        ymin, ymax = plt.ylim()
        plt.ylim(ymax=ymax*1.1)

        # Ajust the window with box legend
        ax = plt.subplot(111)
        box = ax.get_position()
        ax.set_position([box.x0, box.y0 + box.height * 0.1, box.width, box.height * 0.9])

        # for some weird reason we must call savefig before show, otherwise the output file is all white
        plt.savefig('./'+test.name+'.png')
        plt.show()

    #################################################################################
    def test_mini(self):
        print('Comparing and graphing a mini error...')
        t = '../00_install/small.csv'
        r = '../00_install/small_2.csv'
        pb_list = []

        fc = FileComparator(t, r)
        r = fc.compare()

        print('\n### Overall result is: ', r)
        if not r:
            pb_list = fc.get_different_var_tuples()
            print('should graph', str(len(pb_list)), 'variables')

        # for every couple of variables with problems, generate a png
        for v_tuple in pb_list:
            test, ref = v_tuple
            self.generate_png(test, ref)

        self.assertFalse(r)

    #################################################################################
    def test_equals(self):
        print('comparing a file to itself')
        fp = '../00_install/test_214.csv'
        pb_list = []

        fc = FileComparator(fp, fp)
        r = fc.compare()

        print('\n### Overall result is: ', r)
        if not r:
            pb_list = fc.get_different_var_tuples()
            print('should graph', str(len(pb_list)), 'variables')

        # for every couple of variables with problems, generate a png
        for v_tuple in pb_list:
            test, ref = v_tuple
            self.generate_png(test, ref)

        self.assertTrue(r)

    #################################################################################
    def test_diff(self):
        print('Comparing to a known error...')
        t = '../00_install/test_214.csv'
        r = '../00_install/ref_214.csv'
        pb_list = []

        fc = FileComparator(t, r)
        r = fc.compare()

        print('\n### Overall result is: ', r)
        if not r:
            pb_list = fc.get_different_var_tuples()
            print('should graph', str(len(pb_list)), 'variables')

        # for every couple of variables with problems, generate a png
        for v_tuple in pb_list:
            test, ref = v_tuple
            self.generate_png(test, ref)

        self.assertFalse(r)

if __name__ == '__main__':
    unittest.main()