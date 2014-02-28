from queue import Queue, Empty
from threading import Thread
from time import sleep
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot

__author__ = 'saflores'


class sleeper():
    def sleep(self):
        res = 0
        for i in range(10):
            print("sleeping", i)
            sleep(1)
            res += i
        return res


class BackgroundJobWatcher(QObject):
    # this is very strange for me as (an occasional)  Python programmer
    # but must pass a class as an argument (like telling the type of it)
    # I have found that object <built-in> does a good job here.
    JOB_FINISHED = pyqtSignal(object)

    def __init__(self):
        QObject.__init__(self)
        self.test_str = 'can see this instance variables'
        print('WATCHER constructor', self.test_str)


    @pyqtSlot()
    def work(self):
        # the following line will produce an error!
        # we can not see outside this method when in another thread?
        # print('QObj slot :', self.test_str)
        my_sleeper = sleeper()
        res = my_sleeper.sleep()

        self.JOB_FINISHED.emit(str(res))


