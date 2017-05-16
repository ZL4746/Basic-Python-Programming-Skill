class Fraction:

    def __init__(self,numerator,denominator):
        self.num = numerator
        self.den = denominator

    def __str__(self):
        return str(self.num) + " / " + str(self.den)

    def __add__(self,other):
        newden = self.den*other.den
        newnum = self.num*other.den + other.num*self.den

        commonFactor = gcd(newnum,newden)
        return Fraction(newnum//commonFactor,newden//commonFactor)

def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n
        m = oldn
        n = oldm%oldn
    return(n)

def main():

    twoThirds = Fraction(1,4)
    print(twoThirds)

    threeFourths = Fraction(1,4)
    print(threeFourths)

    sum = twoThirds + threeFourths
    print(sum)

main()
