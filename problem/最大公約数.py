#最大公約数
def GCD(x,y):
        if x%y==0:
            return y
        else:
            return GCD(x,x%y)
