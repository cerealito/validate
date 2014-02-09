__author__ = 'cerealito'
import matplotlib.pyplot as plt
from os.path import abspath, exists

def generate_png(test, ref):

    output_f = test.name + '.png'

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
    plt.savefig(output_f)
    #plt.show()
    if exists(output_f):
        return abspath(output_f)
    else:
        return None