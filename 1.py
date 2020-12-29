import random
class TQuadrangle:
    def __init__(self):
        self.a = int(input('введіть значення першої сторони '))
        self.b = int(input('введіть значення другої сторони '))

    def s(self):
        return self.a * self.b

    def p(self):
        return (self.a + self.b) * 2

class Tpryamok(TQuadrangle):
    def __init__(self,a,b):
        super().__init__(a,b)
        if self.a == self.b:
            print('це не прямокутник')

class Tsc(Tpryamok):
    def __init__(self):
            self.a = int(input('введіть значення сторони '))
            self.b = self.a

class Tparalel(Tsc):
    def __init__(self):
        super().__init__()

sum = 0
n = int(input('введіть значення n'))
for i in range(n):
    k = int(random.random() * 4)
    if k == 1:
        p = Tpryamok()
        sum += p.s()
    elif k == 2:
        p = Tsc()
        sum += p.s()
    elif k == 3:
        p = Tparalel()
        sum += p.p()

print(sum)