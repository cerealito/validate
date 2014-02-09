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
        res = fc.compare()

        print('\n### Overall result is: ', res.files_are_equal)
        if not res.files_are_equal:
            pb_list = fc.get_different_var_tuples()
            print('Errors exist (' + str(len(pb_list)) + ')')

        # for every couple of variables with problems, generate a png
        for result in fc.get_results():
            self.generate_png(result.test_var, result.ref_var)

        self.assertFalse(res.files_are_equal)

    #################################################################################
    def test_equals(self):
        print('comparing a file to itself')
        fp = '../00_install/test_214.csv'
        pb_list = []

        fc = FileComparator(fp, fp)
        res = fc.compare()

        print('\n### Overall result is: ', res.files_are_equal)
        if not res.files_are_equal:
            pb_list = fc.get_different_var_tuples()
            print('Errors exist (' + str(len(pb_list)) + ')')

        # for every couple of variables with problems, generate a png
        for result in fc.get_results():
            self.generate_png(result.test_var, result.ref_var)

        self.assertTrue(res.files_are_equal)

    #################################################################################
    def test_diff(self):
        print('Comparing to a known error...')
        t = '../00_install/test_214.csv'
        r = '../00_install/ref_214.csv'
        pb_list = []

        fc = FileComparator(t, r)
        res = fc.compare()

        print('\n### Overall result is: ', res.files_are_equal)
        if not res.files_are_equal:
            pb_list = fc.get_different_var_tuples()
            print('Errors exist (' + str(len(pb_list)) + ')')

        # for every couple of variables with problems, generate a png
        for result in fc.get_results():
            self.generate_png(result.test_var, result.ref_var)

        self.assertFalse(res.files_are_equal)

if __name__ == '__main__':
    unittest.main()