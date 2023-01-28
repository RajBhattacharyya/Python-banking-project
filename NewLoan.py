import loanCheck
import pickle
import random

def loannew(userGivenNumber):
    ln=loanCheck.loanchk(userGivenNumber)
    if ln==2:
        print("You already have an active loan. \nBefore you take a new loan you must repay your old loan")
    elif ln==1:
        print("Your income is less than the required income necessary for loan. \nSorry you are not eligible for loan")
    elif ln==0:   
        lnn={}
        print("Our Bank provide loan at very low interest rates. \n============================================ \nWe provide different kinds of loan. \n1. Home Loan \n2. Car Loan \n3. Business Loan \n4. Education Loan \n5. Personal Loan")
        while True:
            choice=int(input("Enter 1, 2, 3, 4, 5: "))
            print("--.--.--.--.--.--.--")
            if choice==1:
                loanType="Home Loan"
                print("We provide home loan @6.65 p.a")
                loanInterest=6.65
                break
            elif choice==2:
                loanType="Car Loan"
                print("We provide car loan @7.70 p.a")
                loanInterest=7.70
                break
            elif choice==3:
                loanType="Business Loan"
                print("We provide Business loan @11.10 p.a")
                loanInterest=11.10
                break
            elif choice==4:
                loanType="Education Loan"
                print("We provide education loan @9.15 p.a")
                loanInterest=9.15
                break
            elif choice==5:
                loanType="Personal Loan"
                print("We provide personal loan @9.60 p.a")
                loanInterest=9.60
                break
            else:
                print("You entered wrong input.")
                continue
        while True:
            loanAmt=int(input("Enter Loan Amount (Minimum 100000): "))
            if loanAmt>=100000:
                break
            else:
                continue
        while True:
            print("We provide loan for 4-20 yrs")
            loanYears=int(input("Enter the time period for your loan(4-20): "))
            if loanYears>=4 and loanYears<=20:
                break
            else:
                continue
        collateral=input("Enter the details of your collateral: ")
        guarantor=input("Enter the name of your guarantor(If the person dies the guarantor will pay the loan): ")
        totalAmt=int(loanAmt*(pow((1 + loanInterest/100), loanYears)))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        while True:
            conf=input("Do you want to continue? (Y/N): ")
            if conf.upper()=="Y":
                lid=random.randint(1,1000000)
                fth=open("Loan.dat","ab")
                lnn['Loan id']=lid
                lnn['User Name']=userGivenNumber
                lnn['Loan Type']=loanType
                lnn['Loan Amount']=loanAmt
                lnn['Loan Period']=loanYears
                lnn['Interest']=loanInterest
                lnn['Total Amt']=totalAmt
                lnn['Col Details']=collateral
                lnn['Guarantor']=guarantor
                pickle.dump(lnn, fth)
                fth.close()
                alo="Yes"
                fg=open("Banking.dat","rb+")
                sd={}
                try:
                    while True:
                        d=fg.tell()
                        sd=pickle.load(fg)
                        if sd['Account no']==userGivenNumber:
                            sd['Active loan']="Yes"
                            print("Your Loan is approved. \nYour loan id no. is ", lid)
                        fg.seek(d)
                        pickle.dump(sd, fg)
                except EOFError:
                    fg.close()
                break
            elif conf.upper()=="N":
                print("Sorry your loan not approved.")
                break
            else:
                continue
    else:
        print("THANK YOU")