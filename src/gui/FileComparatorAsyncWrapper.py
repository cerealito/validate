from PyQt5 import QtGui
from time import sleep
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, QThread
from FileComparator import FileComparator

__author__ = 'saflores'

class FileComparatorAsyncWrapper(QObject):
    # This is very strange for me as (an occasional) Python programmer.
    # We must pass a class as an argument (like telling the type of it)
    # I have found that object <built-in> does a good job here.
    result_ready = pyqtSignal(object)

    def __init__(self):
        QObject.__init__(self)
        # this is not needed but i used it to learn and experiment
        self.test_str = 'can see this instance variables'
        print('WATCHER constructor', self.test_str)

        self.file_comparator = None

    def set_file_comparator(self, file_comparator_p: FileComparator):
        self.file_comparator = file_comparator_p

    @pyqtSlot()
    def synchronous_compare(self):
        # the following line will produce an error!
        # we can not see outside this method when in another thread?
        # update: the above is only true IF the caller context disappears
        # eg. a local object FileComparatorAsyncWrapper will not exist while
        # this method actually lives on on a separate thread.
        # TODO: write a blog entry on this
        print('QObj slot :', self.test_str)

        # for i in range(5):
        #     sleep(1)
        #     print('sleeping', i)

        comparision_result = self.file_comparator.compare()

        # move this object back to the main thread, were it was originally created
        self.moveToThread(QtGui.QGuiApplication.instance().thread())
        self.result_ready.emit(comparision_result)

