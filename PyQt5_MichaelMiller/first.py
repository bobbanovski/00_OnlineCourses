import sys
from PyQt5.QtWidgets import *
app = QApplication(sys.argv) # Create Application
# dlgMain = QWidget() # Main GUI Canvas
dlgMain = QMainWindow()
dlgMain.setWindowTitle("My GUI")

dlgMain.show()

# app.exec_() # Start processing the event loop
sys.exit(app.exec_()) # appexec passes error code to sysexit on close
#standard python method for closing application