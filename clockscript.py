import sys
import os
import threading
import time
from datetime import datetime
from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.QtGui import QFont, QPixmap
import matrix_generator as m_g

class Ui(QtWidgets.QMainWindow):

    def __init__(self):
        dirname = os.path.dirname(__file__)
        qtUIFile = os.path.join(dirname, "UIFILE\\DATACLOCK.ui")
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi(qtUIFile, self) # Load the .ui file
        self.setfontandsize()
        
         # Show the GUI
        self.t = threading.Thread(target=self.handler)
        self.t.daemon = True
        self.t.start()
        self.updateclock()
        self.show()
    def closeEvent(self, event):
        try:
            event.accept() # let the window close
        except:
            event.ignore()
        else:
            sys.exit()
    def setfontandsize(self):
        defaultfont = QFont('Arial',48,QFont.Bold)

        self.HOUR10.setFont(defaultfont)
        self.HOUR.setFont(defaultfont)
        self.MINUTE10.setFont(defaultfont)
        self.MINUTE.setFont(defaultfont)
        self.SECOND10.setFont(defaultfont)
        self.SECOND.setFont(defaultfont)
    def handler(self):
        while(True):
            time.sleep(1)
            self.updateclock()

    def updateclock(self):
        alllabels = self.HOUR10,self.HOUR,self.MINUTE10,self.MINUTE,self.SECOND10,self.SECOND
        hour = datetime.now().time().hour
        minute = datetime.now().time().minute
        second = datetime.now().time().second
        print("{0} : {1} : {2}".format(hour,minute,second))
        pixpaths = HOUR10px,HOURpx,MINUTE10px,MINUTEpx,SECOND10px,SECONDpx = self.generate_dm_time(
            round(hour/10 - (hour%10)/10),
            hour%10,
            round(minute/10 - (minute%10)/10),
            minute%10,
            round(second/10 - (second%10)/10),
            second%10
                                )
        pixmap = []
        i = 0
        for path in pixpaths:
            pixmap.append(QPixmap(path))
            
        for label in alllabels:
            label.setPixmap(pixmap[i].scaledToHeight(200))
            i+=1

    def generate_dm_time(self,hour10,hour,minute10,minute,second10,second):
        HOUR10px = m_g.generate(hour10,"HOUR10TEMP")
        HOURpx = m_g.generate(hour,"HOURTEMP")
        MINUTE10px = m_g.generate(minute10,"MINUTE10TEMP")
        MINUTEpx = m_g.generate(minute,"MINUTETEMP")
        SECOND10px = m_g.generate(second10,"SECOND10TEMP")
        SECONDpx = m_g.generate(second,"SECONDTEMP")

        return HOUR10px,HOURpx,MINUTE10px,MINUTEpx,SECOND10px,SECONDpx

app = QtWidgets.QApplication(sys.argv) # Create an instance of QtWidgets.QApplication
window = Ui() # Create an instance of our class
app.exec_() # Start the application