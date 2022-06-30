class Fraction:

    def __init__(self,s,m,s1,m1):
        self.sorat=s
        self.makhraj=m

        self.sorat1=s1
        self.makhraj1=m1


    def sum(self):
        Fraction={}
        Fraction.sorst=(self.soorat * self.makhraj1) + (self.makhraj * self.soorat1)
        Fraction.denom=self.sorat1*self.makhraj
        return Fraction   

    def mul(self):
        Fraction={}
        Fraction.sorst=self.sorat*self.sorat
        Fraction.denom=self.makhraj*self.makhraj1
        return Fraction   

    def sub(self):
        Fraction={}
        Fraction.sorst=(self.soorat * self.makhraj1) - (self.makhraj * self.soorat1)
        Fraction.denom=self.makhraj*self.makhraj1
        return Fraction  

    

    def div(self):
        Fraction={}
        Fraction.sorst=self.sorat*self.makhraj1
        Fraction.denom=self.makhraj*self.sorat1
        return Fraction 

    def show(self):
        print(self.soorat, '/', self.makhraj)


    

sorat=int(input("pleas type the sorat: "))
makhraj=int(input("pleas type the makhraj: ")) 
sorat1=int(input("pleas type the sorat1: "))
makhraj1=int(input("pleas type the makhraj1: ")) 

a =(sorat,makhraj)
b = (sorat1,makhraj1)

c = a.sub(b)
c.show()

m=a.mul(b)
m.show()

s=a.sum(b)
s.show()

sub=a.subtract(b)
sub.show()

div=a.div(b)
div.show()