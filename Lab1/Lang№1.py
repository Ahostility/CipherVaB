'''Teory Formal Language

"This code was created by Mikhail Tretyak
and the right to dispose of it remains with him(c)"

Task №1
Create a grammar that generates a formal language
L(G) = {_|_(01)^n_|_ | n>0}
'''

class LangForm:
    def __init__(self,alph,n):
        self.abc = alph
        self.count = n
        self.enter = self.enterLang()

    def P(self,count):
        if count == 1:
            return "01"
        elif count >= 2:
            return str(self.abc[0])+str(self.abc[1]) + str(self.P(count - 1))

    def enterLang(self):
        if self.count <= 0:
            return "Error Validation"
        else:
            string = "_|_" + self.P(self.count) + "_|_"
            return string

ABC = [0,1]
try:
    count = int(input())
except ValueError: count = 0
lang = LangForm(ABC,count)
print(lang.enter)

