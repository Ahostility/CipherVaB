from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Request1(object):
    def setupUi(self, Request1):
        Request1.setObjectName("Request1")
        Request1.resize(595, 500)
        self.label = QtWidgets.QLabel(Request1)
        self.label.setGeometry(QtCore.QRect(60, 10, 231, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Request1)
        self.label_2.setGeometry(QtCore.QRect(30, 330, 61, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Request1)
        self.label_3.setGeometry(QtCore.QRect(310, 330, 61, 16))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(Request1)
        self.pushButton.setGeometry(QtCore.QRect(130, 420, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Request1)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 420, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Request1)
        self.pushButton_3.setGeometry(QtCore.QRect(370, 420, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.textEdit = QtWidgets.QTextEdit(Request1)
        self.textEdit.setGeometry(QtCore.QRect(40, 40, 511, 281))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(Request1)
        self.textEdit_2.setGeometry(QtCore.QRect(30, 350, 221, 41))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(Request1)
        self.textEdit_3.setGeometry(QtCore.QRect(310, 350, 221, 41))
        self.textEdit_3.setObjectName("textEdit_3")

        self.retranslateUi(Request1)
        QtCore.QMetaObject.connectSlotsByName(Request1)

    def retranslateUi(self, Request1):
        _translate = QtCore.QCoreApplication.translate
        Request1.setWindowTitle(_translate("Request1", "Form"))
        self.label.setText(_translate("Request1", "OriginText"))
        self.label_2.setText(_translate("Request1", "KeyNum1"))
        self.label_3.setText(_translate("Request1", "KeyNum2"))
        self.pushButton.setText(_translate("Request1", "Encription"))
        self.pushButton_2.setText(_translate("Request1", "Decription"))
        self.pushButton_3.setText(_translate("Request1", "Clear"))
