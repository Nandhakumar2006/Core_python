# def registor(name,location,prefix="Mr/Miss/Mrs"):
#     if location =="salem":
#         print(prefix,name,"has approved in",location)
#     elif location =='chennai':
#         print(prefix,name,"has gone under waiting state since its",location)
#     else:print("bussinous not approved")

# registor("zealous tech corp","salem","Mr.")
# registor("priya automolies","chennai","Mrs.")
# registor("has been completed","sss")


#list
#index always starts with 0,1,2,3....
balance=[200000,19000,3400,10999]

def debit(money=0,pos=0):
    if money <=balance[pos]:
        balance[pos]-=money
        print(money,"debuted")
        return balance[pos]
    else:print("can't debit")
    
hai=debit(1000,1)
print(hai)



 