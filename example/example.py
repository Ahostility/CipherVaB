#helo Vigener and Boufort12
from example.TestInterface import Ui_MainWindow
from example.WinShifrV import Ui_ShifrV
from example.WinShifrB import Ui_ShifrB
from example.outShifrAnswer import Ui_outShifr
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton

class outWindow(QWidget):
    def __init__(self):
        super(outWindow, self).__init__()
        self.answ = Ui_outShifr()
        self.answ.setupUi(self)

    def clearWin(self):
        self.answ.textEdit.clear()
        self.answ.textEdit_2.clear()

    def closeWin(self):
        pass

    def openTextWinV(self):
        pass

    def openTextWinB(self):
        pass

class WindowButtonLang(QWidget):
    def __init__(self):
        super(WindowButtonLang, self).__init__()
        self.setWindowTitle('Language')
        self.setMinimumWidth(250)
        self.setMinimumHeight(50)
        self.button = QPushButton(self)
        self.button.move(10,10)
        self.button.setText('Rus')
        self.button.show()
        self.button1 = QPushButton(self)
        self.button1.move(80, 10)
        self.button1.setText('Eng')
        self.button1.show()

class Window2V(QWidget):
    def __init__(self):
        super(Window2V, self).__init__()
        self.winV = Ui_ShifrV()
        self.winV.setupUi(self)
        self.winV.textEdit.setPlainText("")
        self.winV.textEdit_2.setPlainText("")
        self.answer = outWindow()

    def ruLang(self):
        abcRu = []
        for i in range(1040, 1072):
            abcRu.append(chr(i))
        self.abc = abcRu
        self.winV.pushButton.clicked.connect(self.encryptUse)
        # self.winV.pushButton.clicked.connect(self.close)
        self.winV.pushButton_2.clicked.connect(self.decryptUse)
        # self.winV.pushButton_2.clicked.connect(self.close)
        self.winV.pushButton_3.clicked.connect(self.clearText)

    def engLang(self):
        abcEng = []
        for i in range(65,91):
            abcEng.append(chr(i))
        self.abc = abcEng
        self.winV.pushButton.clicked.connect(self.encryptUse)
        # self.winV.pushButton.clicked.connect(self.close)
        self.winV.pushButton_2.clicked.connect(self.decryptUse)
        # self.winV.pushButton_2.clicked.connect(self.close)
        self.winV.pushButton_3.clicked.connect(self.clearText)

    def clearText(self):
        self.winV.textEdit.clear()
        self.winV.textEdit_2.clear()

    def encryptUse(self):
        self.answer.show()
        self.key = self.winV.textEdit_2.toPlainText()
        self.our_text = self.winV.textEdit.toPlainText()
        shifr = self.shifr_Vigera()
        self.answer.answ.textEdit.setPlainText(shifr)
        self.answer.answ.pushButton_3.clicked.connect(self.answer.clearWin)
        self.answer.answ.pushButton_3.clicked.connect(self.answer.close)

    def decryptUse(self):
        self.answer.show()
        self.key = self.winV.textEdit_2.toPlainText()
        self.shifr = self.winV.textEdit.toPlainText()
        old_text = self.decoding_shifr()
        self.answer.answ.textEdit_2.setPlainText(old_text)
        self.answer.answ.pushButton_3.clicked.connect(self.answer.clearWin)
        self.answer.answ.pushButton_3.clicked.connect(self.answer.close)

    def shifr_Vigera(self):
        shifrotext = ""
        a = []
        k = 0
        n = 0
        index_str = 0
        index_pil = 0
        newkey = ""
        for i in range(len(self.our_text)):
            newkey += self.key[i % len(self.key)]
        for i in range(len(self.abc)):
            a.append([])
            for j in range(len(self.abc)):
                a[i].append(self.abc[(j + i) % len(self.abc)])
        while n != len(self.our_text):
            for ind in range(len(self.abc)):
                if a[ind][0] == self.our_text[k % len(newkey)]:
                    index_str = ind
                    for str in range(len(self.abc)):
                        if a[0][str] == newkey[k % len(newkey)]:
                            index_pil = str
                            shifrotext += a[index_str][index_pil]
            k += 1
            n += 1
        return shifrotext

    def decoding_shifr(self):
        old_text = ""
        a = []
        k = 0
        n = 0
        index_str = 0
        newkey = ""
        for i in range(len(self.shifr)):
            newkey += self.key[i % len(self.key)]
        for i in range(len(self.abc)):
            a.append([])
            for j in range(len(self.abc)):
                a[i].append(self.abc[(j + i) % len(self.abc)])
        while n != len(self.shifr):
            for ind in range(len(self.abc)):
                if a[0][ind] == newkey[k % len(newkey)]:
                    for str in range(len(self.abc)):
                        if a[str][ind] == self.shifr[k % len(self.shifr)]:
                            index_str = str
                            old_text += a[index_str][0]
            k += 1
            n += 1
        return old_text

class Window2B(QWidget):
    def __init__(self):
        super(Window2B, self).__init__()
        self.winB = Ui_ShifrB()
        self.winB.setupUi(self)
        self.answer = outWindow()

    def ruLang(self):
        abcRu = []
        for i in range(1040, 1072):
            abcRu.append(chr(i))
        self.abc = abcRu
        self.winB.pushButton.clicked.connect(self.encryptUse)
        # self.winB.pushButton.clicked.connect(self.close)
        self.winB.pushButton_2.clicked.connect(self.decryptUse)
        # self.winB.pushButton_2.clicked.connect(self.close)
        self.winB.pushButton_3.clicked.connect(self.clearText)

    def engLang(self):
        abcEng = []
        for i in range(65, 91):
            abcEng.append(chr(i))
        self.abc = abcEng
        self.winB.pushButton.clicked.connect(self.encryptUse)
        # self.winB.pushButton.clicked.connect(self.close)
        self.winB.pushButton_2.clicked.connect(self.decryptUse)
        # self.winB.pushButton_2.clicked.connect(self.close)
        self.winB.pushButton_3.clicked.connect(self.clearText)

    def clearText(self):
        self.winB.textEdit.clear()
        self.winB.textEdit_2.clear()

    def encryptUse(self):
        self.answer.show()
        self.key = self.winB.textEdit_2.toPlainText()
        self.our_text = self.winB.textEdit.toPlainText()
        shifr = self.shifr_Bofora()
        self.answer.answ.textEdit.setPlainText(shifr)
        self.answer.answ.pushButton_3.clicked.connect(self.answer.clearWin)
        self.answer.answ.pushButton_3.clicked.connect(self.answer.close)

    def decryptUse(self):
        self.answer.show()
        self.key = self.winB.textEdit_2.toPlainText()
        self.shifr = self.winB.textEdit.toPlainText()
        old_text = self.decoding_Bofora()
        self.answer.answ.textEdit_2.setPlainText(old_text)
        self.answer.answ.pushButton_3.clicked.connect(self.answer.clearWin)
        self.answer.answ.pushButton_3.clicked.connect(self.answer.close)

    def shifr_Bofora(self):
        shifr = ""
        a = []
        k = 0
        n = 0
        index_str = 0
        newkey = ""
        for i in range(len(self.our_text)):
            newkey += self.key[i % len(self.key)]
        for i in range(len(self.abc)):
            a.append([])
            for j in range(len(self.abc)):
                a[i].append(self.abc[(j + i) % len(self.abc)])
        while n != len(self.our_text):
            for ind in range(len(self.abc)):
                if a[0][ind] == self.our_text[k % len(self.our_text)]:
                    for str in range(len(self.abc)):
                        if a[str][ind] == newkey[k % len(newkey)]:
                            index_str = str
                            shifr += a[index_str][0]
            k += 1
            n += 1
        return shifr

    def decoding_Bofora(self):
        old_text = ""
        a = []
        k = 0
        n = 0
        index_pil = 0
        newkey = ""
        for i in range(len(self.shifr)):
            newkey += self.key[i % len(self.key)]
        for i in range(len(self.abc)):
            a.append([])
            for j in range(len(self.abc)):
                a[i].append(self.abc[(j + i) % len(self.abc)])
        while n != len(self.shifr):
            for str in range(len(self.abc)):
                if a[str][0] == self.shifr[k % len(newkey)]:
                    for ind in range(len(self.abc)):
                        if a[str][ind] == newkey[k % len(newkey)]:
                            index_pil = ind
                            old_text += a[0][ind]
            k += 1
            n += 1
        return old_text

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self. win = Ui_MainWindow()
        self.win.setupUi(self)
        self.win.radioButton.clicked.connect(self.shifrViginer)
        self.win.radioButton_2.clicked.connect(self.shifrBofor)

    def shifrViginer(self):
        self.win21 = Window2V()
        self.win21.show()
        self.win1 = WindowButtonLang()
        self.win1.show()
        self.win1.button.clicked.connect(self.win21.ruLang)
        self.win1.button.clicked.connect(self.win1.close)
        self.win1.button1.clicked.connect(self.win21.engLang)
        self.win1.button1.clicked.connect(self.win1.close)

    def shifrBofor(self):
        self.win22 = Window2B()
        self.win22.show()
        self.win1 = WindowButtonLang()
        self.win1.show()
        self.win1.button.clicked.connect(self.win22.ruLang)
        self.win1.button.clicked.connect(self.win1.close)
        self.win1.button1.clicked.connect(self.win22.engLang)
        self.win1.button1.clicked.connect(self.win1.close)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    api = MainWindow()
    api.show()
    sys.exit(app.exec_())
