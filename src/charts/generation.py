__author__ = 'cerealito'
import matplotlib.pyplot as plt
from os.path import abspath, exists


def generate_png(test, ref):

    output_f = test.name + '.png'

    plt.plot(ref.times(), ref.values(), color='#00FF21',
             label='ref', linestyle='solid', linewidth=2.5)
    plt.plot(test.times(), test.values(), color='#FF1D00',
             label='test', linestyle='dashed', linewidth=1.5)
    plt.title(test.name)
    plt.ylabel('value')
    plt.xlabel('seconds')
    # one
    plt.legend(ncol=1, loc=1)

    # get the min and max values in the Y axis
    ymin, ymax = plt.ylim()
    # set the y axis to be drawn 30% more than the default
    plt.ylim(ymax=ymax*1.3)


    # for some weird reason we must call savefig before show, otherwise the output file is all white
    plt.savefig(output_f, dpi=240, bbox_inches='tight')
    #plt.show()
    plt.close()
    if exists(output_f):
        return abspath(output_f)
    else:
        return None


########################################################################################################################
def show(test, ref):
    plt.plot(ref.times(), ref.values(), color='#00FF21',
             label='ref', linestyle='solid', linewidth=2.5)
    plt.plot(test.times(), test.values(), color='#FF1D00',
             label='test', linestyle='dashed', linewidth=1.5)
    plt.title(test.name)
    plt.ylabel('value')
    plt.xlabel('seconds')
    # one
    plt.legend(ncol=1, loc=1)

    # get the min and max values in the Y axis
    ymin, ymax = plt.ylim()
    # set the y axis to be drawn 30% more than the default
    plt.ylim(ymax=ymax*1.3)

    plt.show()
    plt.close()
