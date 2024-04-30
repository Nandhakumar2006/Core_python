# for car in "Nandhakumar":
#     print(car)

# beta={1000,2500,"Nandhakumar",6.0}
# for n in beta:
#     print(n)

# tup=("nandha",4500.5,"kumar","wipro",True)
# for q in tup:
#     print(q)
# pos=0
# while pos<len(tup):
#     print(tup[pos])
#     pos+=1

# pos=2
# while pos<len(tup):
#     print(tup[pos])
#     pos+=1

# pos=0
# while pos<len(tup)-2:
#     print(tup[pos])
#     pos+=1

stock=10
for stock in range(5,0,-1):
    amt=int(input("enter the amouunt"))
    if amt>=10000:
        print("stock quantity one has purchased")
        stock-=1
    else:
        print("insufficient amount to purchase") 