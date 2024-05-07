s=("sam","nandhakumar",4,4,5)
print(s)
print(type(s))

#range in tuple or slicing method
a=("annamalai","nandhakuar","mohan","navin","krishna")
print(a[0:4])
print(a[:2])
print(a[2:])

a=10
b=10.5
c="nandhakumar"
print(type(a))
print(type(b))
print(type(c))


#tuple method
a=(1,2,3,4,5,6,1,8,3,4,1,510,1)
b=a.count(1)
print(b)

#index
s=(1,2,3,4,5,6,7)
d=s.index(2)
print(d)


#append method
a=("annamalai","nandhakuar","mohan","navin","krishna")
b=list(a)
b.append("gokul")
a=tuple(b)
print(a)

#adding tuple in tuple
a=("annamalai","nandhakuar","mohan","navin","krishna")
b=("gokul",)
a += b
print(a)

a=("annamalai","nandhakuar","mohan","navin","krishna")
if "navin" in a:
    print("welcome")
else:
    print("not valid")



#join 
a=("annamalai","nandhakuar","mohan","navin","krishna")
b=(1,2,3,4,5)
c= a+b
print(c)

a=("annamalai","nandhakuar","mohan","navin","krishna")
for i in a:
    print(i)

#range methods
a=(1,2,3,"sam","nandhakumar")
for i in range(len(a)):
    print(a[i])


#remove
a=("annamalai","nandhakuar","mohan","navin","krishna")
b=list(a)
b.remove("navin")
a=tuple(b)
print(a)