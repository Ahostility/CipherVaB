import sys
import random
from Lab1.Lab1 import *
from Lab2.Cezar import *
from Lab3.pleyferUpdate import *
from Lab4.lab4 import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from TitleCrypto import Ui_TitleWindow
from WinLab1 import Ui_Lab1
from WinLab2 import Ui_Lab2
from WinLab3 import Ui_Lab3
from WinLab4 import Ui_Lab4
from Request1 import Ui_Request1
from Answer import Ui_Answer

class Answer(QWidget):
    def __init__(self):
        super(Answer,self).__init__()
        self.answer = Ui_Answer()
        self.answer.setupUi(self)
        self.answer.textEdit.setPlainText("")
        self.answer.textEdit_2.setPlainText("")
        self.answer.pushButton.clicked.connect(self.clearAnswer)

    def clearAnswer(self):
        self.answer.textEdit.clear()
        self.answer.textEdit_2.clear()


class Request11(QWidget):
    def __init__(self):
        super(Request11,self).__init__()
        self.req11 = Ui_Request1()
        self.req11.setupUi(self)
        self.answer1 = Answer()
        self.req11.textEdit.setPlainText("")
        self.req11.textEdit_2.setPlainText("")
        self.req11.textEdit_3.setPlainText("")
        self.req11.pushButton.clicked.connect(self.encription)
        self.req11.pushButton_2.clicked.connect(self.decription)
        self.req11.pushButton_3.clicked.connect(self.clearText)

    def encription(self):
        self.answer1.show()
        self.origin = self.req11.textEdit.toPlainText()
        our_text = self.origin.upper()
        self.key1 = self.req11.textEdit_2.toPlainText()
        keyList1 = [int(i) for i in self.key1]

        self.key2 = self.req11.textEdit_3.toPlainText()
        keyList2 = [int(i) for i in self.key2]

        shifrCezar = str(double_permutation_enc(keyList1,keyList2,our_text))
        self.answer1.answer.textEdit.setPlainText(shifrCezar)

    def decription(self):
        self.answer1.show()
        self.origin = self.req11.textEdit.toPlainText()
        our_text = self.origin.upper()
        self.key1 = self.req11.textEdit_2.toPlainText()
        keyList1 = [int(i) for i in self.key1]

        self.key2 = self.req11.textEdit_3.toPlainText()
        keyList2 = [int(i) for i in self.key2]

        shifrCezar = str(double_permutation_dec(keyList1, keyList2, our_text))
        self.answer1.answer.textEdit.setPlainText(shifrCezar)

    def clearText(self):
        self.req11.textEdit.clear()
        self.req11.textEdit_2.clear()
        self.req11.textEdit_3.clear()

class Request12(QWidget):
    def __init__(self):
        super(Request12,self).__init__()
        self.req12 = Ui_Request1()
        self.req12.setupUi(self)
        self.answer1 = Answer()
        self.req12.textEdit.setPlainText("")
        self.req12.textEdit_2.setPlainText("")
        self.req12.textEdit_3.setPlainText("")
        self.req12.pushButton.clicked.connect(self.encription)
        self.req12.pushButton_2.clicked.connect(self.decription)
        self.req12.pushButton_3.clicked.connect(self.clearText)

    def encription(self):
        self.answer1.show()
        self.origin = self.req12.textEdit.toPlainText()
        our_text = self.origin.upper()
        self.key1 = self.req12.textEdit_2.toPlainText()
        keyList1 = [int(i) for i in self.key1]
        # keyList1 = [2,4,1,7,3,8,6,5]

        cipherPerm = str(permutation_enc(our_text,keyList1))
        self.answer1.answer.textEdit.setPlainText(cipherPerm)

    def decription(self):
        self.answer1.show()
        self.origin = self.req12.textEdit.toPlainText()
        our_text = self.origin.upper()
        self.key1 = self.req12.textEdit_2.toPlainText()
        keyList1 = [int(i) for i in self.key1]
        # keyList1 =[2,4,1,7,3,8,6,5]

        cipherPerm = str(permutation_dec(our_text,keyList1))
        self.answer1.answer.textEdit.setPlainText(cipherPerm)

    def clearText(self):
        self.req12.textEdit.clear()
        self.req12.textEdit_2.clear()
        self.req12.textEdit_3.clear()

class Request13(QWidget):
    def __init__(self):
        super(Request13,self).__init__()
        self.req13 = Ui_Request1()
        self.req13.setupUi(self)
        self.answer1 = Answer()
        self.req13.textEdit.setPlainText("")
        self.req13.textEdit_2.setPlainText("")
        self.req13.textEdit_3.setPlainText("")
        self.req13.pushButton.clicked.connect(self.encription)
        self.req13.pushButton_2.clicked.connect(self.decription)
        self.req13.pushButton_3.clicked.connect(self.clearText)

    def encription(self):
        self.answer1.show()
        self.origin = self.req13.textEdit.toPlainText()
        our_text = self.origin.upper()

        self.key = [8,3,4,1,5,9,6,7,2]
        # random.shuffle(key)
        # self.keyRand = key
        # magic = str(magic_square_enc(self.keyRand, our_text))
        magic = str(magic_square_enc(self.key, our_text))
        self.answer1.answer.textEdit.setPlainText(magic)


    def decription(self):
        self.answer1.show()
        self.origin = self.req13.textEdit.toPlainText()
        our_text = self.origin.upper()

        # magic = str(magic_square_dec(self.keyRand, our_text))
        magic = str(magic_square_dec(self.key, our_text))
        self.answer1.answer.textEdit_2.setPlainText(magic)

    def clearText(self):
        self.req13.textEdit.clear()
        self.req13.textEdit_2.clear()
        self.req13.textEdit_3.clear()





class Request21(QWidget):
    def __init__(self):
        super(Request21, self).__init__()
        self.req21 = Ui_Request1()
        self.req21.setupUi(self)
        self.answer2 = Answer()
        self.req21.textEdit.setPlainText("")
        self.req21.textEdit_2.setPlainText("")
        self.req21.textEdit_3.setPlainText("")
        self.req21.pushButton.clicked.connect(self.encription)
        self.req21.pushButton_2.clicked.connect(self.decription)
        self.req21.pushButton_3.clicked.connect(self.clearText)

    def encription(self):
        self.answer2.show()
        self.origin = self.req21.textEdit.toPlainText()
        our_text = self.origin.upper()
        self.key1 = self.req21.textEdit_2.toPlainText()
        keyIntC = int(self.key1.upper())
        abc = createABC2()
        shifrCezar = str(Cezar(our_text,abc,keyIntC))
        self.answer2.answer.textEdit.setPlainText(shifrCezar)

    def decription(self):
        self.answer2.show()
        self.origin = self.req21.textEdit.toPlainText()
        our_text = self.origin.upper()
        self.key1 = self.req21.textEdit_2.toPlainText()
        keyIntC = int(self.key1.upper())
        abc = createABC2()
        shifrCezar = str(decriptCezar(our_text,abc,keyIntC))
        self.answer2.answer.textEdit_2.setPlainText(shifrCezar)

    def clearText(self):
        self.req21.textEdit.clear()
        self.req21.textEdit_2.clear()
        self.req21.textEdit_3.clear()

class Request22(QWidget):
    def __init__(self):
        super(Request22,self).__init__()
        self.req22 = Ui_Request1()
        self.req22.setupUi(self)
        self.answer2 = Answer()
        self.req22.textEdit.setPlainText("")
        self.req22.textEdit_2.setPlainText("")
        self.req22.textEdit_3.setPlainText("")
        self.req22.pushButton.clicked.connect(self.encription)
        self.req22.pushButton_2.clicked.connect(self.decription)
        self.req22.pushButton_3.clicked.connect(self.clearText)


    def encription(self):
        self.answer2.show()
        self.origin = self.req22.textEdit.toPlainText()
        our_text = self.origin.upper()
        self.key1 = self.req22.textEdit_2.toPlainText()
        keyInt1 = int(self.key1.upper())
        self.key2 = self.req22.textEdit_3.toPlainText()
        keyInt2 = int(self.key2.upper())
        abc = createABC2()
        self.shifrAphine = aphineCezar(our_text, abc, keyInt1,keyInt2)
        self.answer2.answer.textEdit.setPlainText(str(self.shifrAphine[0]))

    def decription(self):
        self.answer2.show()
        self.origin = self.req22.textEdit.toPlainText()
        our_text = self.origin.upper()
        self.key1 = self.req22.textEdit_2.toPlainText()
        keyInt1 = int(self.key1.upper())
        self.key2 = self.req22.textEdit_3.toPlainText()
        keyInt2 = int(self.key2.upper())
        abc = createABC2()
        index = self.shifrAphine[1]
        shifrAphine = decriptaphineCezar(our_text,index, abc, keyInt1, keyInt2)
        self.answer2.answer.textEdit_2.setPlainText(str(shifrAphine))

    def clearText(self):
        self.req22.textEdit.clear()
        self.req22.textEdit_2.clear()
        self.req22.textEdit_3.clear()

class Request23(QWidget):
    def __init__(self):
        super(Request23, self).__init__()
        self.req23 = Ui_Request1()
        self.req23.setupUi(self)
        self.answer2 = Answer()
        self.req23.textEdit.setPlainText("")
        self.req23.textEdit_2.setPlainText("")
        self.req23.textEdit_3.setPlainText("")
        self.req23.pushButton.clicked.connect(self.encription)
        self.req23.pushButton_2.clicked.connect(self.decription)
        self.req23.pushButton_3.clicked.connect(self.clearText)

    def encription(self):
        self.answer2.show()
        self.origin = self.req23.textEdit.toPlainText()
        our_text = self.origin.upper()
        self.key1 = self.req23.textEdit_2.toPlainText()
        keyWord = self.key1.upper()
        self.key2 = self.req23.textEdit_3.toPlainText()
        keyIntC = int(self.key2.upper())
        abc = createABC2()

        cipherCezar = str(cezarWithKeyWord(our_text,abc,keyWord,keyIntC))
        self.answer2.answer.textEdit.setPlainText(cipherCezar)


    def decription(self):
        self.answer2.show()
        self.origin = self.req23.textEdit.toPlainText()
        our_text = self.origin.upper()
        self.key1 = self.req23.textEdit_2.toPlainText()
        keyWord = self.key1.upper()
        self.key2 = self.req23.textEdit_3.toPlainText()
        keyIntC = int(self.key2.upper())
        abc = createABC2()
        cipherCezar = str(decriptcezarWithKeyWord(our_text, abc, keyWord, keyIntC))
        self.answer2.answer.textEdit_2.setPlainText(cipherCezar)

    def clearText(self):
        self.req23.textEdit.clear()
        self.req23.textEdit_2.clear()
        self.req23.textEdit_3.clear()

class Request24(QWidget):
    def __init__(self):
        super(Request24,self).__init__()
        self.req24 = Ui_Request1()
        self.req24.setupUi(self)
        self.answer2 = Answer()
        self.req24.textEdit.setPlainText("")
        self.req24.textEdit_2.setPlainText("")
        self.req24.textEdit_3.setPlainText("")
        self.req24.pushButton.clicked.connect(self.encription)
        self.req24.pushButton_2.clicked.connect(self.decription)
        self.req24.pushButton_3.clicked.connect(self.clearText)


    def encription(self):
        self.answer2.show()
        self.origin = self.req24.textEdit.toPlainText()
        our_text = self.origin.upper()
        self.key1 = self.req24.textEdit_2.toPlainText()
        keyWord = self.key1.upper()
        abc = createABC2()
        cipherCezar = str(trisemus(our_text, abc, keyWord))
        self.answer2.answer.textEdit.setPlainText(cipherCezar)

    def decription(self):
        self.answer2.show()
        self.origin = self.req24.textEdit.toPlainText()
        our_text = self.origin.upper()
        self.key1 = self.req24.textEdit_2.toPlainText()
        keyWord = self.key1.upper()
        abc = createABC2()
        cipherCezar = str(decriptionTris(our_text, abc, keyWord))
        self.answer2.answer.textEdit_2.setPlainText(cipherCezar)

    def clearText(self):
        self.req24.textEdit.clear()
        self.req24.textEdit_2.clear()
        self.req24.textEdit_3.clear()

class Request3(QWidget):
    def __init__(self):
        super(Request3,self).__init__()
        self.req3 = Ui_Request1()
        self.req3.setupUi(self)
        self.answer3 = Answer()
        self.req3.textEdit.setPlainText("")
        self.req3.textEdit_2.setPlainText("")
        self.req3.textEdit_3.setPlainText("")
        self.req3.pushButton.clicked.connect(self.encription)
        self.req3.pushButton_2.clicked.connect(self.decription)
        self.req3.pushButton_3.clicked.connect(self.clearText)

    def encription(self):
        self.answer3.show()
        self.origin = self.req3.textEdit.toPlainText()
        our_text = self.origin.upper()
        self.key1 = self.req3.textEdit_2.toPlainText()
        abc = createABC2()
        print(abc)

        shifrPleyfer = str(playfair_encode(our_text,abc,self.key1))
        self.answer3.answer.textEdit.setPlainText(shifrPleyfer)

    def decription(self):
        pass

    def clearText(self):
        self.req3.textEdit.clear()
        self.req3.textEdit_2.clear()
        self.req3.textEdit_3.clear()

class Request41(QWidget):
    def __init__(self):
        super(Request41,self).__init__()
        self.req41 = Ui_Request1()
        self.req41.setupUi(self)
        self.answer4 = Answer()
        self.req41.textEdit.setPlainText("")
        self.req41.textEdit_2.setPlainText("")
        self.req41.textEdit_3.setPlainText("")
        self.req41.pushButton.clicked.connect(self.encription)
        self.req41.pushButton_2.clicked.connect(self.decription)
        self.req41.pushButton_3.clicked.connect(self.clearText)

    def encription(self):
        self.answer4.show()
        self.origin = self.req41.textEdit.toPlainText()
        our_text = self.origin.upper()
        self.key1 = self.req41.textEdit_2.toPlainText()
        key1 = self.key1.upper()
        self.abc =[]
        for i in range(1040, 1072):
            self.abc.append(chr(i))
        shifr= str(cipherViginer(our_text,self.abc,key1))
        self.answer4.answer.textEdit.setPlainText(shifr)

    def decription(self):
        self.answer4.show()
        self.origin = self.req41.textEdit.toPlainText()
        our_text = list(self.origin.upper())
        self.key1 = self.req41.textEdit_2.toPlainText()
        key1 = self.key1.upper()
        self.abc = []
        for i in range(1040, 1072):
            self.abc.append(chr(i))
        shifr = str(decriptionViginer(our_text, self.abc, key1))
        self.answer4.answer.textEdit_2.setPlainText(shifr)

    def clearText(self):
        self.req41.textEdit.clear()
        self.req41.textEdit_2.clear()
        self.req41.textEdit_3.clear()

class Request42(QWidget):
    def __init__(self):
        super(Request42,self).__init__()
        self.req42 = Ui_Request1()
        self.req42.setupUi(self)
        self.answer4 = Answer()
        self.req42.textEdit.setPlainText("")
        self.req42.textEdit_2.setPlainText("")
        self.req42.textEdit_3.setPlainText("")
        self.req42.pushButton.clicked.connect(self.encription)
        self.req42.pushButton_2.clicked.connect(self.decription)
        self.req42.pushButton_3.clicked.connect(self.clearText)

    def encription(self):
        self.answer4.show()
        self.origin = self.req42.textEdit.toPlainText()
        our_text = self.origin.upper()
        shifr = str(winston_enc(our_text))
        self.answer4.answer.textEdit.setPlainText(shifr)


    def decription(self):
        pass

    def clearText(self):
        self.req42.textEdit.clear()
        self.req42.textEdit_2.clear()
        self.req42.textEdit_3.clear()




class WindowLab1(QWidget):
    def __init__(self):
        super(WindowLab1, self).__init__()
        self.winLab1 = Ui_Lab1()
        self.winLab1.setupUi(self)
        self.winLab1.radioButton.clicked.connect(self.openReq1)
        self.winLab1.radioButton_2.clicked.connect(self.openReq2)
        self.winLab1.radioButton_3.clicked.connect(self.openReq3)

    def openReq1(self):
        self.req11 = Request11()
        self.req11.show()

    def openReq2(self):
        self.req12 = Request12()
        self.req12.show()

    def openReq3(self):
        self.req13 = Request13()
        self.req13.show()

class WindowLab2(QWidget):
    def __init__(self):
        super(WindowLab2, self).__init__()
        self.winLab2 = Ui_Lab2()
        self.winLab2.setupUi(self)
        self.winLab2.radioButton.clicked.connect(self.openReq1)
        self.winLab2.radioButton_2.clicked.connect(self.openReq2)
        self.winLab2.radioButton_3.clicked.connect(self.openReq3)
        self.winLab2.radioButton_4.clicked.connect(self.openReq4)

    def openReq1(self):
        self.req21 = Request21()
        self.req21.show()

    def openReq2(self):
        self.req22 = Request22()
        self.req22.show()

    def openReq3(self):
        self.req23 = Request23()
        self.req23.show()

    def openReq4(self):
        self.req24 = Request24()
        self.req24.show()

class WindowLab3(QWidget):
    def __init__(self):
        super(WindowLab3, self).__init__()
        self.winLab3 = Ui_Lab3()
        self.winLab3.setupUi(self)
        self.winLab3.radioButton.clicked.connect(self.openReq)


    def openReq(self):
        self.req3 = Request3()
        self.req3.show()

class WindowLab4(QWidget):
    def __init__(self):
        super(WindowLab4, self).__init__()
        self.winLab4 = Ui_Lab4()
        self.winLab4.setupUi(self)
        self.winLab4.radioButton.clicked.connect(self.openReq1)
        self.winLab4.radioButton_2.clicked.connect(self.openReq2)

    def openReq1(self):
        self.req41 = Request41()
        self.req41.show()
    def openReq2(self):
        self.req42 = Request42()
        self.req42.show()

class TitleWindow(QMainWindow):
    def __init__(self):
        super(TitleWindow,self).__init__()
        self.win = Ui_TitleWindow()
        self.win.setupUi(self)
        self.win.radioButton.clicked.connect(self.lab1)
        self.win.radioButton_2.clicked.connect(self.lab2)
        self.win.radioButton_3.clicked.connect(self.lab3)
        self.win.radioButton_4.clicked.connect(self.lab4)

    def lab1(self):
        self.winLab1 = WindowLab1()
        self.winLab1.show()

    def lab2(self):
        self.winLab2 = WindowLab2()
        self.winLab2.show()

    def lab3(self):
        self.winLab3 = WindowLab3()
        self.winLab3.show()

    def lab4(self):
        self.winLab4 = WindowLab4()
        self.winLab4.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    api = TitleWindow()
    api.show()
    sys.exit(app.exec_())