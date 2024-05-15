class college:
    def getStudentInfo(self):
        self.__rollno=input("enter the roll number:")
        self.__name=input("enter the name:")

    def printStudentInfo(self):
        print("roll number :",self.__rollno,"name:",self.__name)

class BE(college):
    def getBE(self):
        self.getStudentInfo()
        self.__p = int(input("enter the physics mark"))
        self.__c = int(input("enter the chemistry mark"))
        self.__m = int(input("enter the maths mark"))

    def printBE(self):
        self.printStudentInfo()
        print("Marks in different subjects ",self.__p,self.__c,self.__m)

    def calctotalmarks (self):
        return(self.__p+self.__m+self.__c)
    
class Result(BE):
    def getResult(self):
        self.getBE()
        self.__total=self.calctotalmarks()

    def putResult(self):
        self.printBE()
        print("total marks out of 300;", self.__total)

college=Result()
college.getResult()
college.putResult()