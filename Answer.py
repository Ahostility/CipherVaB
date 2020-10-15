from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Answer(object):
    def setupUi(self, Answer):
        Answer.setObjectName("Answer")
        Answer.resize(671, 447)
        self.textEdit = QtWidgets.QTextEdit(Answer)
        self.textEdit.setGeometry(QtCore.QRect(40, 30, 271, 361))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(Answer)
        self.textEdit_2.setGeometry(QtCore.QRect(350, 30, 271, 361))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label = QtWidgets.QLabel(Answer)
        self.label.setGeometry(QtCore.QRect(40, 10, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Answer)
        self.label_2.setGeometry(QtCore.QRect(350, 10, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Answer)
        self.pushButton.setGeometry(QtCore.QRect(300, 410, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Answer)
        QtCore.QMetaObject.connectSlotsByName(Answer)

    def retranslateUi(self, Answer):
        _translate = QtCore.QCoreApplication.translate
        Answer.setWindowTitle(_translate("Answer", "Form"))
        self.label.setText(_translate("Answer", "Encription"))
        self.label_2.setText(_translate("Answer", "Decription"))
        self.pushButton.setText(_translate("Answer", "OK"))
