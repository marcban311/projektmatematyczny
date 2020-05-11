from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QAction, QInputDialog,QLineEdit,QFileDialog, QLabel, QScrollArea
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton



class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(434, 429)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

#okno witające
        self.label_wprowadzenie = QtWidgets.QLabel(self.centralwidget)
        self.label_wprowadzenie.setGeometry(QtCore.QRect(6, 12, 411, 16))
        self.label_wprowadzenie.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_wprowadzenie.setObjectName("label_wprowadzenie")

#checkbox masa
        self.checkBox_masa = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_masa.setGeometry(QtCore.QRect(130, 40, 111, 16))
        self.checkBox_masa.setObjectName("checkBox_masa")
        self.checkBox_masa.stateChanged.connect(lambda state: self.clickchbox(
                state, self.groupBox_masa))

#checkbox wsp
        self.checkBox_wsp = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_wsp.setGeometry(QtCore.QRect(10, 40, 111, 16))
        self.checkBox_wsp.setObjectName("checkBox_wsp")
        self.checkBox_wsp.stateChanged.connect(lambda state: self.clickchbox(
                state, self.groupBox_wsp))


#checkbox  kąt     
        self.checkBox_kat = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_kat.setGeometry(QtCore.QRect(250, 40, 111, 16))
        self.checkBox_kat.setObjectName("checkBox_kat")
        self.checkBox_kat.stateChanged.connect(lambda state: self.clickchbox(
                state, self.groupBox_kat))

#groupbox i lebel wsp
        self.groupBox_wsp = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_wsp.setGeometry(QtCore.QRect(10, 90, 131, 91))
        self.groupBox_wsp.setTitle("")
        self.groupBox_wsp.setObjectName("groupBox_wsp")
        self.groupBox_wsp.setDisabled(1)

        self.label_wsp = QtWidgets.QLabel(self.groupBox_wsp)
        self.label_wsp.setGeometry(QtCore.QRect(10, 20, 71, 16))
        self.label_wsp.setObjectName("label_wsp")
   
#okno do wpisywania wsp
        self.textedit_wsp = QtWidgets.QTextEdit(self.groupBox_wsp)
        self.textedit_wsp.setGeometry(QtCore.QRect(10, 40, 111, 31))
        self.textedit_wsp.setObjectName("textedit_wsp")
        self.textedit_wsp.textChanged.connect(self.zmiana_wsp)
        self.textedit_wsp_value = 0

#groupbox i lebel masa
        self.groupBox_masa = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_masa.setGeometry(QtCore.QRect(150, 90, 131, 91))
        self.groupBox_masa.setTitle("")
        self.groupBox_masa.setObjectName("groupBox_masa")
        self.groupBox_masa.setDisabled(1)

        self.label_masa = QtWidgets.QLabel(self.groupBox_masa)
        self.label_masa.setGeometry(QtCore.QRect(10, 20, 91, 16))
        self.label_masa.setObjectName("label_masa")

#okno do wpisywania wsp
        self.textedit_masa = QtWidgets.QTextEdit(self.groupBox_masa)
        self.textedit_masa.setGeometry(QtCore.QRect(10, 40, 101, 31))
        self.textedit_masa.setObjectName("textedit_masa")

#groupbox i lebel kąt 
        self.groupBox_kat = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_kat.setGeometry(QtCore.QRect(290, 90, 131, 91))
        self.groupBox_kat.setTitle("")
        self.groupBox_kat.setObjectName("groupBox_kat")
        self.groupBox_kat.setDisabled(1)

        self.label_kat = QtWidgets.QLabel(self.groupBox_kat)
        self.label_kat.setGeometry(QtCore.QRect(10, 20, 101, 16))
        self.label_kat.setObjectName("label_kat")

#okno do wpisywania kąta
        self.textedit_kat = QtWidgets.QTextEdit(self.groupBox_kat)
        self.textedit_kat.setGeometry(QtCore.QRect(10, 40, 101, 31))
        self.textedit_kat.setObjectName("textedit_kat")
        

# oknowyświetlające wynik
        self.Label_wynikft = QtWidgets.QLabel(self.centralwidget)
        self.Label_wynikft.setGeometry(QtCore.QRect(10, 190, 411, 21))
        self.Label_wynikft.setObjectName("Label_wynikft")

        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 434, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionExit)
        self.actionExit.triggered.connect(self.close_app)

        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.menuFile.addAction(self.actionSave)
        self.actionSave.triggered.connect 
        
        
        self.menubar.addAction(self.menuFile.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Program Matematyczny"))
        self.label_wprowadzenie.setText(_translate("MainWindow", "Witaj w programie wyliczającym siłę tarcia. Początkowo zaznacz wartości które znasz. "))
        self.checkBox_masa.setText(_translate("MainWindow", "masa obiektu"))
        self.checkBox_wsp.setText(_translate("MainWindow", "wsp. tarcia"))
        self.checkBox_kat.setText(_translate("MainWindow", "kąt nachylenia "))
        self.label_wsp.setText(_translate("MainWindow", "Wsp. tarcia"))
        self.label_masa.setText(_translate("MainWindow", "Masa obiektu w kg"))
        self.label_kat.setText(_translate("MainWindow", "Kąt nachylenia "))
        self.Label_wynikft.setText(_translate("MainWindow", "TextLabel"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionExit.setText(_translate("MainWindow", "Zamknij"))
        self.actionExit.setStatusTip(_translate("MainWindow", "Zamyka program"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionSave.setText(_translate("MainWindow", "Zapisz"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
    
    def zmiana(self, state,):
        new_value = self.textedit_wsp.toPlainText()

        print("new_value", new_value)
        print("self.textedit_wsp_value", self.textedit_wsp_value)
        new_value = new_value.replace(",", ".")    
        if len(new_value) == 0:
                self.textedit_wsp.setPlainText("0")
                self.textedit_wsp_value = 0
        else:

                try:
                        new_value = float(new_value)
                        self.textedit_wsp_value = new_value
                except:
                        new_value = self.textedit_wsp_value
                        self.textedit_wsp.setPlainText(str(new_value))

    def zmiana_wsp(self):
        new_value = self.textedit_wsp.toPlainText()

        print("new_value", new_value)
        print("self.textedit_wsp_value", self.textedit_wsp_value)

        new_value = new_value.replace(",", ".")
        
        if len(new_value) == 0:
                self.textedit_wsp.setPlainText("0")
                self.textedit_wsp_value = 0
        else:

                try:
                        new_value = float(new_value)
                        self.textedit_wsp_value = new_value
                except:
                        new_value = self.textedit_wsp_value
                        self.textedit_wsp.setPlainText(str(new_value))

    def clickchbox(self, state, box):
        if state == QtCore.Qt.Checked:
                print('Checked')
                box.setDisabled(0)
        else:
                print('Unchecked')
                box.setDisabled(1)
    
    def close_app(self):
        sys.exit()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())