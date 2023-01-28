import pickle

def deposit(userGivenNumber, k):
    ft=open("Banking.dat","rb+")
    sd={}
    fd=False
    try:
        while True:
            b = ft.tell()
            sg = pickle.load(ft)
            if sg['Account no']==userGivenNumber:
                if k==1:
                    depositAmount=int(input("Enter the amount you want to deposit: "))
                    while True:
                        if depositAmount>0:
                            sg['Balance']=sg['Balance']+depositAmount
                            break
                        else:
                            depositAmount=int(input("Re-Enter the amount you want to deposit: "))
                else:
                    chequeNum=int(input("Enter cheque number: "))
                    depositAmount=int(input("Enter the amount of the cheque: "))
                    while True:
                        if depositAmount>0:
                            sg['Balance']=sg['Balance']+depositAmount
                            print("Your cheque of number", chequeNum, "is processing...... \nPlease wait.... ... .. . .")
                            break
                        else:
                            depositAmount=int(input("Re-Enter the amount: "))
                ft.seek(b)
                pickle.dump(sg, ft)
                fd=True
    except EOFError:
        if fd==False:
            print("Transaction Failed")
        else:
            print("Tansaction Successful. \nYour current balance is", sg['Balance'])
        ft.close()