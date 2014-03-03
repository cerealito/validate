from PyQt5 import QtGui
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, QThread
from FileComparator import FileComparator

__author__ = 'saflores'

class FileComparatorAsyncWrapper(QObject):
    # This is very strange for me as (an occasional) Python programmer.
    # We must pass a class as an argument (like telling the type of it)
    # I have found that object <built-in> does a good job here.
    result_ready = pyqtSignal(object)

    sig_error_ocurred = pyqtSignal(object)

    def __init__(self):
        QObject.__init__(self)
        # this is not needed but i used it to learn and experiment
        self.test_str = 'can see this instance variables'
        print('WATCHER constructor', self.test_str)

        #self.file_comparator = None
        self.test_file = None
        self.ref_file = None

    def set_files_to_compare(self, test_file, ref_file):
        self.test_file = test_file
        self.ref_file = ref_file

    @pyqtSlot()
    def synchronous_compare(self):
        # the following line will produce an error!
        # we can not see outside this method when in another thread?
        # update: the above is only true IF the caller context disappears
        # eg. a local object FileComparatorAsyncWrapper will not exist while
        # this method actually lives on on a separate thread.
        # TODO: write a blog entry on this
        print('QObj slot :', self.test_str)
        comparision_result = None
        ########## try to create our (synchronous) file comparator
        try:
            fc = FileComparator(self.test_file, self.ref_file)
            comparision_result = fc.compare()
        except UnicodeDecodeError:
            self.sig_error_ocurred.emit('Format not recognized')
        except Exception as e:
            self.sig_error_ocurred.emit(str(e))
        finally:
            # move this object back to the main thread, were it was originally created
            # right before emitting the signal and even if errors occurred
            self.moveToThread(QtGui.QGuiApplication.instance().thread())

        if comparision_result:
            self.result_ready.emit(comparision_result)