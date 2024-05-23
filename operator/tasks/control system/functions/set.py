# #duplicates
# a={"nandhakumar","navin","krishna","mohan","mohan","gokul"}
# print(a)
# print(type(a))
# print(len(a))
# print(a)

# #set constructor
# s=set(("nandhakumar","navin","krishna"))
# print(s)

# #uptade set
# ss={"nandhakumar","navin","krishna","mohan","mohan","gokul"}
# ss.update("aravind")
# print(ss) 

#iteratable
a={"nandhakumar","navin","mohan","gokul"}
li=["aravind"]
a.update(li)
print(a)
a.discard(2)
print(a)

# #pop method
# #access method
a={"nandhakumar","navin","krishna","mohan","mohan","gokul"}
for i in a:
    print(i)

# #check the set is present or not
# a={"nandhakumar","navin","krishna","mohan","mohan","gokul"}
# print("mohan" in a)
