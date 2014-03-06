from time import sleep
from PyQt5.QtCore import QThread, QCoreApplication, QObject, pyqtSignal
import sys

class Ticker(QObject):
    finished = pyqtSignal()
    def tick_10(self):
        for i in range(5):
            print(str(i), 'ticker.tick_10 is executed in', QThread.currentThread())
            sleep(1)

        original = QCoreApplication.instance().thread()
        print ('done, moving back to', original)
        self.moveToThread(original)
        self.finished.emit()

##########################
myApp = QCoreApplication(sys.argv)

print("              From main thread:", QThread.currentThread())
print("                        my APP:", myApp.thread())
t = QThread()
t = QThread()
print('  Created new thread t with id:', t)
print('  but               t.thread():', t.thread())

ticker = Ticker()
print('new ticker lives in           :', ticker.thread())
print()
t.started.connect(ticker.tick_10)
ticker.finished.connect(t.deleteLater)

ticker.moveToThread(t)
t.start()

myApp.exec()


