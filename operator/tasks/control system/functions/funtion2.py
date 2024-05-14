# def greet():
#     ans=input("tell us ur desired city")
#     if ans =="chennai":print("too dangerous to live")
#     elif ans =="salem":print("safe to go out")
#     elif ans =="villupuram":print("don't evr think to go")
#     else:print("stay wher you are")
# greet()

def prompt(qual,ref):
    if qual == 'ug' and ref == 'HR':
        print("you are in the uk team")
    elif qual == 'diploma' and ref =='testlead':
        print('test associate')
    elif qual == 'diploma' and ref == 'test lead':
        print("team associate")
    else:print("you are hired")

    prompt('engg','project manager')
    prompt('ug','HR')
    prompt(ref='testlead',qual='diploma')

