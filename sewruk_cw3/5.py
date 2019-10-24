class Calculator():
    def __init__(self):
        pass

    def add(self,a,b):
        return a+b
    def difference(self,a,b):
        return a-b
    def multiply(self,a,b):
        return a*b
    def divide(self,a,b):
        if(b!=0):
            return a/b
        else:
            print("nie dziel przez zero!!!")



moj_kalk = Calculator()

print(moj_kalk.add(2,3))
print(moj_kalk.divide(4,0.000001))