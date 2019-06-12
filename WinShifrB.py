# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WinShifrB.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ShifrB(object):
    def setupUi(self, ShifrB):
        ShifrB.setObjectName("ShifrB")
        ShifrB.resize(550, 360)
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(12)
        ShifrB.setFont(font)
        self.textEdit = QtWidgets.QTextEdit(ShifrB)
        self.textEdit.setGeometry(QtCore.QRect(10, 40, 520, 250))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(ShifrB)
        self.label.setGeometry(QtCore.QRect(10, 10, 210, 24))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(ShifrB)
        self.pushButton.setGeometry(QtCore.QRect(130, 330, 75, 24))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(ShifrB)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 330, 75, 24))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(ShifrB)
        self.pushButton_3.setGeometry(QtCore.QRect(330, 330, 75, 24))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_2 = QtWidgets.QLabel(ShifrB)
        self.label_2.setGeometry(QtCore.QRect(20, 300, 47, 21))
        self.label_2.setObjectName("label_2")
        self.textEdit_2 = QtWidgets.QTextEdit(ShifrB)
        self.textEdit_2.setGeometry(QtCore.QRect(50, 300, 361, 24))
        self.textEdit_2.setObjectName("textEdit_2")

        self.retranslateUi(ShifrB)
        QtCore.QMetaObject.connectSlotsByName(ShifrB)

    def retranslateUi(self, ShifrB):
        _translate = QtCore.QCoreApplication.translate
        ShifrB.setWindowTitle(_translate("ShifrB", "Shifr_Bofora"))
        self.label.setText(_translate("ShifrB", "You message:"))
        self.pushButton.setText(_translate("ShifrB", "Encryption"))
        self.pushButton_2.setText(_translate("ShifrB", "Decryption"))
        self.pushButton_3.setText(_translate("ShifrB", "Clear"))
        self.label_2.setText(_translate("ShifrB", "Key:"))


