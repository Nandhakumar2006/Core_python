# seat=1
# while seat<=15:
#     amt=int(input("Tell is amount"))
#     if amt>=190:
#         print("Ticketd Booked",seat)
#     else:
#         print("Insufficient amount") 



hire=5
while hire>0:
    skill=input("tell us the skill you knew: ")
    poc=int(input("tell us how many project done on"+skill+":"))
    if(skill=="java" or skill =="python") and poc>=4:
        print("you are recriuted to our company")
    elif(skill=="HTML") and poc>=2:
        print("you are transfered to the sub company of one of ours")
        hire-=1
    else:
        print("try to uptade skill /work more poc")