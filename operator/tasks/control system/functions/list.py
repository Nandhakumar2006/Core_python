# prop=["Nandhakumar",5.5,80,"n"]
# print(prop)

# prop.append("software developer")
# print(prop)
# print(len(prop))

# prop.insert(4,25.5)
# print(prop)

# prop[5]="team lead"
# print(prop)

# monthly=[5000,30000,6500,7000,3000]
# print(min(monthly))
# print(sum(monthly))
# monthly.remove(30000)
# print(monthly)
# print(monthly.pop())
# print(monthly.pop(1))
# print(monthly)
# print(monthly.reverse())
# print(monthly)

# sum=[4000,500,555,888,444]
# print(sum)
# print(sum.pop())
# print(sum.pop(3))
# print(sum)
# sum.reverse()
# print(sum)

# lis=[1,4,5,6,1,5,8]
# a=lis.copy()
# print("copy:",a)
# count=a.count(1)
# print(count)

# a=input("enter the name")
# list=a.split(",")
# print("list names")
# for i in list:
#     print(i)
 
n=int(input("enter the list"))
List1=[]
for i in range(n):
    lival=input("enter the list:")
    List1.append(lival)
print("list:",List1)