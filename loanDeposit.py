import pickle
import loanClose

def loandep(lid, userGivenNumber):
    ft=open("Loan.dat","rb")
    sd={}
    amt=0
    try:
        while True:
            sg = pickle.load(ft)
            if sg['Loan id']==lid:
                amt=sg['Total Amt']
    except EOFError:
        ft.close()
    print("Amount left to repay the loan ", amt)
    dp=int(input("Enter the amount you want to repay: "))
    while True:
        if dp>0:
            if dp<amt:
                fat=open("Loan.dat","rb+")
                std={}
                fd=False
                try:
                    while True:
                        b=fat.tell()
                        sg=pickle.load(fat)
                        if sg['Loan id']==lid:
                            sg['Total Amt']=sg['Total Amt']-dp
                        fat.seek(b)
                        pickle.dump(sg, fat)
                        fd=True
                except EOFError:
                    if fd==False:
                        print("=============================== \nWe are SORRY.... \nTransaction Failed....")
                    else:    
                        print("=============================== \nTansaction Successful. \nLoan amount left", sg['Total Amt'])
                    fat.close()
                    break
            elif dp==amt:
                loanClose.deleteLoan(lid)
                fg=open("Banking.dat","rb+")
                sd={}
                try:
                    while True:
                        d=fg.tell()
                        sd=pickle.load(fg)
                        if sd['Account no']==userGivenNumber:
                            sd['Active loan']="Nil"    
                        fg.seek(d)
                        pickle.dump(sd, fg)
                except EOFError:
                    fg.close()
                break
            else:
                print("Amount you entered execeed the required amount")
                dp=int(input("Re-Enter the amount you want to repay: "))
        else:
            dp=int(input("Re-Enter the amount you want to repay: "))