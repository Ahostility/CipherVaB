from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TitleWindow(object):
    def setupUi(self, TitleWindow):
        TitleWindow.setObjectName("TitleWindow")
        TitleWindow.resize(395, 320)
        self.centralwidget = QtWidgets.QWidget(TitleWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 20, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(30, 110, 82, 17))
        self.radioButton.setObjectName("radioButton")

        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(30, 140, 82, 17))
        self.radioButton_2.setObjectName("radioButton_2")

        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(30, 170, 82, 17))
        self.radioButton_3.setObjectName("radioButton_3")

        self.radioButton_4 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_4.setGeometry(QtCore.QRect(30, 200, 82, 17))
        self.radioButton_4.setObjectName("radioButton_4")

        TitleWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TitleWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 395, 21))
        self.menubar.setObjectName("menubar")
        TitleWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TitleWindow)
        self.statusbar.setObjectName("statusbar")
        TitleWindow.setStatusBar(self.statusbar)

        self.retranslateUi(TitleWindow)
        QtCore.QMetaObject.connectSlotsByName(TitleWindow)

    def retranslateUi(self, TitleWindow):
        _translate = QtCore.QCoreApplication.translate
        TitleWindow.setWindowTitle(_translate("TitleWindow", "MainWindow"))
        self.label.setText(_translate("TitleWindow", "Криптография"))

        self.radioButton.setText(_translate("TitleWindow", "Lab1"))
        self.radioButton_2.setText(_translate("TitleWindow", "Lab2"))
        self.radioButton_3.setText(_translate("TitleWindow", "Lab3"))
        self.radioButton_4.setText(_translate("TitleWindow", "Lab4"))
