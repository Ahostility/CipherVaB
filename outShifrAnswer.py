from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_outShifr(object):
    def setupUi(self, outShifr):
        outShifr.setObjectName("outShifr")
        outShifr.resize(837, 554)
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(12)
        outShifr.setFont(font)
        self.textEdit = QtWidgets.QTextEdit(outShifr)
        self.textEdit.setGeometry(QtCore.QRect(10, 40, 380, 460))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(outShifr)
        self.label.setGeometry(QtCore.QRect(20, 10, 180, 24))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(outShifr)
        self.label_2.setGeometry(QtCore.QRect(440, 10, 180, 24))
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setObjectName("label_2")
        self.textEdit_2 = QtWidgets.QTextEdit(outShifr)
        self.textEdit_2.setGeometry(QtCore.QRect(440, 40, 380, 460))
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton_3 = QtWidgets.QPushButton(outShifr)
        self.pushButton_3.setGeometry(QtCore.QRect(380, 520, 75, 24))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(outShifr)
        QtCore.QMetaObject.connectSlotsByName(outShifr)

    def retranslateUi(self, outShifr):
        _translate = QtCore.QCoreApplication.translate
        outShifr.setWindowTitle(_translate("outShifr", "ShifroText"))
        self.label.setText(_translate("outShifr", "Shifr: Encryption"))
        self.label_2.setText(_translate("outShifr", "Shifr: Decryption"))
        self.pushButton_3.setText(_translate("outShifr", "OK"))


