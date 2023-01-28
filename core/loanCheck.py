import pickle

def loanchk(userGivenNumber):
    fac=open("Banking.dat","rb")
    sta={}
    try:
        while True:
            sta=pickle.load(fac)
            if sta['Account no']==userGivenNumber:
                if sta['Active loan']=='Nil':
                    print("You do not have any active loan therefore you can apply for a loan. \nMinimum salary required is 25000/-")
                    while True:
                        choice=input("Do you want to continue? (Y/N): ")
                        print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
                        if choice.upper()=="Y":
                            if sta['Salary']>=25000:
                                print("You are eligilbe for a loan.....")
                                ln=0
                                break
                            else:
                                ln=1
                                break
                        elif choice.upper()=="N":
                            ln=3
                            break
                        else:
                            continue
                else:
                    ln=2
    except EOFError:
        fac.close()
    return ln