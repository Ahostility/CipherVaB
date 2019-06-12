# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WinShifrV.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ShifrV(object):
    def setupUi(self, ShifrV):
        ShifrV.setObjectName("ShifrV")
        ShifrV.resize(550, 360)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ShifrV.sizePolicy().hasHeightForWidth())
        ShifrV.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(12)
        font.setItalic(False)
        ShifrV.setFont(font)
        ShifrV.setMouseTracking(True)
        ShifrV.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label = QtWidgets.QLabel(ShifrV)
        self.label.setGeometry(QtCore.QRect(9, 9, 210, 24))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(ShifrV)
        self.textEdit.setGeometry(QtCore.QRect(10, 40, 520, 250))
        self.textEdit.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(ShifrV)
        self.pushButton.setGeometry(QtCore.QRect(130, 330, 75, 24))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(ShifrV)
        self.pushButton_3.setGeometry(QtCore.QRect(330, 330, 75, 24))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_2 = QtWidgets.QPushButton(ShifrV)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 330, 75, 24))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(ShifrV)
        self.label_2.setGeometry(QtCore.QRect(20, 300, 47, 21))
        self.label_2.setObjectName("label_2")
        self.textEdit_2 = QtWidgets.QTextEdit(ShifrV)
        self.textEdit_2.setGeometry(QtCore.QRect(50, 300, 361, 24))
        self.textEdit_2.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.textEdit_2.setObjectName("textEdit_2")

        self.retranslateUi(ShifrV)
        QtCore.QMetaObject.connectSlotsByName(ShifrV)

    def retranslateUi(self, ShifrV):
        _translate = QtCore.QCoreApplication.translate
        ShifrV.setWindowTitle(_translate("ShifrV", "Shifr_Viginera"))
        self.label.setText(_translate("ShifrV", "You message:"))
        self.pushButton.setText(_translate("ShifrV", "Encryption"))
        self.pushButton_3.setText(_translate("ShifrV", "Clear"))
        self.pushButton_2.setText(_translate("ShifrV", "Decryption"))
        self.label_2.setText(_translate("ShifrV", "Key:"))


