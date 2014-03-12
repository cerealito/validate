__author__ = 'cerealito'
import matplotlib
matplotlib.use("agg")
import matplotlib.pyplot as plt
from os.path import abspath, exists


def generate_svg(test, ref):
    print("showing svg, current backend at the begining is", plt.get_backend())
    output_f = test.name + '.svg'

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
    # 240 for very high quality. 120 acceptable. 96 is fast but ugly
    # TODO: make this configurable
    plt.savefig(output_f, dpi=240, bbox_inches='tight')
    # use clf instead of close, otherwise pyplot will crash in windows the second time!
    # clearing somehow is necessary for pdf files with more than one chart
    plt.clf()
    if exists(output_f):
        return abspath(output_f)
    else:
        return None
