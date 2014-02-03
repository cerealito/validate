import unittest
from src.FileComparator import FileComparator
import matplotlib.pyplot as plt

__author__ = 'saflores'

class graph_tester(unittest.TestCase):

    def test_mini(self):
        print('Comparing and graphing a mini error...')
        t = '../00_install/small.csv'
        r = '../00_install/small_2.csv'

        fc = FileComparator(t, r)

        r = fc.compare()

        print('\n### Overall result is: ', r)
        if not r:
            pb_list = fc.get_different_var_tuples()
            print('should graph', str(len(pb_list)), 'variables')

            for v_tuple in pb_list:
                test, ref = v_tuple

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
                plt.show()

        self.assertFalse(r)

    def test_equals(self):
        print('comparing a file to itself')
        fp = '../00_install/test_214.csv'

        fc = FileComparator(fp, fp)

        r = fc.compare()

        print('\n### Overall result is: ', r)
        if not r:
            pb_list = fc.get_different_var_tuples()
            print('should graph', str(len(pb_list)), 'variables')
        self.assertTrue(r)

    def test_diff(self):
        print('Comparing to a known error...')
        t = '../00_install/test_214.csv'
        r = '../00_install/ref_214.csv'

        fc = FileComparator(t, r)
        r = fc.compare()

        print('\n### Overall result is: ', r)
        if not r:
            pb_list = fc.get_different_var_tuples()
            print('should graph', str(len(pb_list)), 'variables')

            for v_tuple in pb_list:
                test, ref = v_tuple

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
                plt.show()

        self.assertFalse(r)

if __name__ == '__main__':
    unittest.main()