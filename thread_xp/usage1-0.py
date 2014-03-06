
from PyQt5.QtCore import QThread, QCoreApplication
import sys, time

class CustomThread(QThread):
    def run(self):
        for i in range(10):
            print(str(i), 'from work thread:', self.currentThreadId())
            time.sleep(1)
        return


myApp = QCoreApplication(sys.argv)
print("  From main thread:", QThread.currentThreadId())

t = CustomThread()
t.finished.connect(myApp.quit)

t.start()

myApp.exec()


