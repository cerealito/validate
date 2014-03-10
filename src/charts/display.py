__author__ = 'saflores'
import platform
import matplotlib.pyplot as plt


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
    # do not close in Mac OSX to avoid strange white square errors
    if platform.system() == 'Windows':
        plt.close()
