from PyQt5.QtCore import QSettings

__author__ = 'cerealito'
import matplotlib
matplotlib.use("agg")
import matplotlib.pyplot as plt
import os
from os.path import abspath, exists, join


def generate_png(test, ref, output_dir=None):
    output_f = test.name + '.png'

    if output_dir:
        if not exists(output_dir):
            os.makedirs(output_dir)
        output_f = join(output_dir, output_f)

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
    # 240 for very high quality. 110 acceptable. 70 is fast but ugly
    mySettings = QSettings(QSettings.IniFormat, QSettings.UserScope, 'Sogeti', 'validate')

    # image quality value is 110 by default, unless the user set it to something else
    image_q = 110
    if mySettings.contains('report/imageQuality'):
        image_q = int(mySettings.value('report/imageQuality'))

    plt.savefig(output_f, dpi=image_q, bbox_inches='tight')
    # use clf instead of close, otherwise pyplot will crash in windows the second time!
    # clearing somehow is necessary for pdf files with more than one chart
    plt.clf()
    if exists(output_f):
        return abspath(output_f)
    else:
        return None
