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


class ScienceCalculator(Calculator):
    def __init__(self):
        pass

    def powerty(self,a,b):
        return pow(a,b)



moj_kalk = ScienceCalculator()

print(moj_kalk.add(2,3))
print(moj_kalk.divide(4,0.000001))
print(moj_kalk.powerty(4,2))