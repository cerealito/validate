
from PyQt5.QtCore import QThread, QCoreApplication, QObject
import sys, time

class CustomObject(QObject):
    def __init__(self, *args):
        super().__init__(*args)
        print()
        print('custom object lives in', self.thread())
        print('           executes in', QThread.currentThread())

class CustomThread(QThread):
    def __init__(self):
        super().__init__()
        print()
        print('Custom Thread constructor lives in:', self.thread())
        print('                       executes in:', self.currentThread())
        print()

    def run(self):
        print()
        print('Custom Thread.run() lives in:', self.thread())
        print('                executes  in:', self.currentThread())
        print()
        return

#######################################
myApp = QCoreApplication(sys.argv)
print("    main is running in ", QThread.currentThread())
print("        myApp lives in ", myApp.thread())

CustomObject()

t = CustomThread()
t.finished.connect(t.quit)
t.finished.connect(myApp.quit)
t.start()

print('t started, executing app...')

myApp.exec()
