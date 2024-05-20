class account:

    def __init__(self,name="",num=0,bal=0.0):
        print("constructor called")
        self.__holder=name
        self.__accnum=num
        self.__accbal=bal

    def __add__(self,other):
        self.__accbal+=other
        print(other,"credicted",self.__accnum)
    def __sub__(self,other):
        if self.__accbal>=other:
            self.__accbal-=other
            print(other,"debited",self.__accnum)
        else:
            print(self.__accnum,"insuuficient balance")


    def __str__(self):
        return self.__holder+" "+str(self.__accnum)+" "+str(self.__accbal)+"\n"
    

    def setholder(self,name=""):self.__holder=name
    def getholder(self):return self.__holder
    def setaccnum(self,num=0):self.__accnum=num
    def getaccnum(self):return self.__accnum
    def setaccbal(self,bal=0.0):self.__accbal=bal
    def getaccbal(self):return self.__accbal

acc1=account()
acc1.setaccnum(545445544)
acc1.setaccbal(5000.0)
acc1.setholder("Nandhakumar")
print(acc1)
acc1+4000
print(acc1)

acc2=account("ram",78979469,7000.8)
print(acc2.getaccbal())