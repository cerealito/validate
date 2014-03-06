
from PyQt5.QtCore import QThread, QCoreApplication
import sys, time

class CustomThread(QThread):
    def __init__(self):
        super().__init__()
        print('     Constructor lives in', self.thread())
        print('              executes in', self.currentThread())
        print()

    def run(self):
        print()
        for i in range(3):
            print(str(i), 'runf lives in:', self.thread())
            print(str(i), ' executes  in:', self.currentThread())
            print()
            time.sleep(1)
        return


myApp = QCoreApplication(sys.argv)
print("  main is running in ", QThread.currentThread())
print("      myApp lives in ", myApp.thread())
t = CustomThread()
t.finished.connect(t.quit)

t.start()

myApp.exec()
