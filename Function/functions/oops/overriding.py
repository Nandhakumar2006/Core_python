class sam:
    def name(self):
        print("hello")
class raja(sam):
    def name(self):
        super().name()
        print("raja")
class arun(raja):
    def name(self):
        super().name()
        print("arun")

# s=arun()
# s.name()
# s1=raja()
# s1.name()
s2=arun()
s2.name()

    