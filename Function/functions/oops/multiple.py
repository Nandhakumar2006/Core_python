class skillset:
    def __init__(self,name="",exp=0,poc=0):
        self.skill=name
        self.exp=exp
        self.poc=poc
    def view(self):
        return self.skill+" "+str(self.exp)+" "+str(self.poc)
    
class Personal:
        
    def __init__(self,name,qual="",con=0,mail=""):
        self.name=name
        self.qualification=qual
        self.contact=con
        self.mail=mail
    def __str__(self):
        return self.name+" "+self.qualification+" "+str(self.contact)+" "+self.mail
        
#mutiple

class profile(Personal,skillset):
    def __init__(self,user="",q="",c=0,m="",s="",e=0,p=0):
        super(profile,self).__init__(user,q,c,m)
        self.skill=s;self.exp=e;self.poc=p
    def __str__(self):
        return super(profile,self).__str__()+" "+self.view()
    
pro=profile("nandha","CSE",54985,"nandha@gmail.com","core python",10,3)
pro1=profile("annamalai","CSE",2093,"sam@gmail.com","python and java")
print(pro)
print(pro1)