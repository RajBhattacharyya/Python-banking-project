import stdiomask
import pickle

def check(userGivenNumber):
    fileOpen=open("Banking.dat","rb")
    std={}
    found=False
    ty=4
    try:
        while True:
            std=pickle.load(fileOpen)
            if std['Account no']==userGivenNumber:
                while ty>0:
                    passd=stdiomask.getpass("Enter your account password: ")
                    if std['Transaction Password']==passd:
                        print("Account Found.")
                        return True
                        break
                    else:
                        ty=ty-1
                        print("Incorrect Password. Attempt left", ty)
                else:
                    print("Sorry!:( \nYou entered wrong password 4 times! \nYour account can not be accessed :( :(")
                found=True
    except EOFError:
        if found==False:
            print("No such Account found!!! :(")
        fileOpen.close()
    return False