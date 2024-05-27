def gcd(m, n):
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn
    return n


class Fraction(object):
    def __init__(self,top,bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num)+"/"+str(self.den)

    def show(self):
        print(self.num,"/",self.den)

    def __add__(self,other):
        newnum = self.num*other.den + other.num*self.den
        newden = self.den*other.den
        common = gcd(newnum,newden)
        return Fraction(newnum//common,newden//common)

a,b,c,d = map(int,input().split())
f1 = Fraction(a,b)
f2 = Fraction(c,d)
f3=f1+f2
print(f3)
