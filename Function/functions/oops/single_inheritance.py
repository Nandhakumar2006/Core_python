#single inheritance
class Account:
    accountno=0
    accountbal=0.0
    accountholder=""
    def __str__(self):
        return str(self.accountno)+" "+self.accountholder+" "+str(self.accountbal)+"\n"
#single
class Card(Account):
    cardnumber=0
    def __init__(self,cn=0,anum=0,ahold="",abal=0.0):
        self.cardnumber=cn
        self.transactions=[]
        self.accountno=anum
        self.accountholder=ahold
        self.accountbal=abal
    def __add__(self,amt):
        self.accountbal+=amt
        print(amt,"deposited to",self.accountholder)
        self.transactions.append("credit")
    def __sub__(self,draw):
        if self.accountbal>=draw:
            self.accountbal-=draw
            print(draw,"has been withdrawn from ",self.accountholder)
            self.transactions.append("depit")
        else:print("insufficient account balance")
    # def counttrans(self):
    #     crecount=self.transactions.count("credit")
    #     depcount=self.transactions.count("depit")
    #     charges=0
    #     if crecount>=5:
    #         charges+=(crecount-5)*10
    #     if depcount>=3:
    #         charges+=(depcount-3)*20
    #         print("total  charges depited in your account",charges)
    #         self.accountbal-=charges
    #         print("charges debited in your account")
    def __str__(self):
        return str(super(Card, self).__str__())+"\n"+str(self.cardnumber)+" "+str(self.accountbal)+"\n"
a1=Account()
a1.accountno=12345;a1.accountholder="kumar";a1.accountbal=15000.0
print(a1)
c=Card(123,458,"sam",3500.66)
c+1800
print(c)
# c1-200
# c1+1000
# c1-100
# c1-500
# c1+100000
# c1-1000
# c1+4000
# print(c1)
# c1.counttrans()