import pickle
import random
import stdiomask
import NewAccount
import password
import checkAccount
import accountDetails
import modifyAccount
import depositMoney
import transaction
import NewLoan
import loanDetails
import loanDeposit
import deleteAcc

#MAIN                  
print("\t\t\t\t*********************************** \n\t\t\t\t(: WELCOME TO OUR BANKING SYSTEM :) \n\t\t\t\t***********************************")
while True:
    print("1. Want to Create an Account \n2. Login to Existing User \n3. Exit")
    ch=int(input("Enter 1, 2 or 3: "))
    if ch==1:
        print("~~~~~~~~~~~~~~~~~~~~~~ \nSelect an Account type: \n1. Saving \n2. Fixed")
        userAccountChoice=int(input("Choose 1 or 2: "))
        if userAccountChoice==1:
            print("---------------- \nThanking for choosing a Saving account....... \nYou will be getting an interest of 3.5% p.a \nPlease complete the following procedure to create an account. \n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            NewAccount.new(userAccountChoice)
        elif userAccountChoice==2:
            print("------------------ \nThanking for choosing a Fixed account......... \nOur bank provide you with 3 different kind of FD accounts:- \nFD for 5 years @ 7.5% p.a \nFD for 7 years @ 9% p.a \nFD for 10 years @ 12% p.a")
            ten=int(input("Enter a tenure for your Fixed account: (5, 7 or 10): "))
            ed="Please complete the following procedure to create an account. \n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
            if ten==5:
                print("You will be getting an interest of 7.5% p.a \n", ed)
                userAccountChoice=2
                NewAccount.new(userAccountChoice)
            elif ten==7:
                print("You will be getting an interest of 9% p.a \n", ed)
                userAccountChoice=3
                NewAccount.new(userAccountChoice)
            elif ten==10:
                print("You will be getting an interest of 12% p.a \n", ed)
                userAccountChoice=4
                NewAccount.new(userAccountChoice)
            else:
                print("Oops! Incorrect Choice.")
        else:
            print("Oops! Incorrect Choice.")
    elif ch==2:
        print("--------------------")
        userGivenNumber=int(input("Enter account number: "))
        if checkAccount.check(userGivenNumber)==True:
            while True:
                print("~~~~~~~~~~~~~~ \nWhat do you want to do? \n1. Check your account details \n2. Modify your account details \n3. Deposit Money \n4. Withdraw Money \n5. Online Transaction \n6. Loan \n7. Delete Account \n8. Back")
                chk=int(input("Enter 1, 2, 3, 4, 5, 6, 7 or 8: "))
                print("-----------------------------")
                if chk==1:
                    accountDetails.details(userGivenNumber)
                elif chk==2:
                    print("What do you want to modify? \n1. Name \n2. Date of Birth \n3. Aadhaar Number \n4. Mobile No. \n5. Email \n6. Occupation \n7. Salary \n8. Transaction Password \n9. Back") 
                    m=int(input("Choose an Option to modify(1-9): "))
                    if m in range(1, 9):
                        modifyAccount.modify(userGivenNumber, m)
                    elif m==9:
                        continue
                    else:
                        print("Oops! Incorrect Choice.")
                elif chk==3:
                    print("Choose a method for deposting money: \n1. Cash \n2. Cheque \n3. Back")
                    k=int(input("Enter 1, 2 or 3: "))
                    print("~~~~~~~~~~~~~~~")
                    if k==1 or k==2:
                        depositMoney.deposit(userGivenNumber, k)
                    elif k==3:
                        continue
                    else:
                        print("Oops! Incorrect Choice.")
                elif chk==4:
                    a=1
                    transaction.trs(userGivenNumber, a)
                elif chk==5:
                    a=2
                    transaction.trs(userGivenNumber, a)
                elif chk==6:
                    print("(:Welcome to our loan service:) \n1. New loan \n2. Existing loan \n3. Back")
                    ka=int(input("Enter 1, 2 or 3: "))
                    print("~~~~~~~~~~~")
                    if ka==1:
                        NewLoan.loannew(userGivenNumber)
                    elif ka==2:
                        lid=int(input("Enter Loan id: "))
                        lc=open("Loan.dat","rb")
                        fod=False
                        while True:
                            try:
                                lf=pickle.load(lc)
                                if lf['Loan id']==lid:
                                    alw=1
                                    fod=True
                            except EOFError:
                                break
                        if fod==False:
                            alw=0
                        lc.close()
                        if alw==1:
                            while True:
                                print("What you want to do? \n1. Check Loan Details \n2. Deposit Loan amount \n3. Exit")
                                cho=int(input("Choose 1,2 or 3: "))
                                if cho==1:
                                    loanDetails.loandel(lid)
                                elif cho==2:
                                    loanDeposit.loandep(lid, userGivenNumber)
                                    break
                                elif cho==3:
                                    break
                                else:
                                    print("Oops! Incorrect Choice.")
                        else:
                            print("No loan found with id", lid)
                    elif ka==3:
                        continue
                    else:
                        print("Oops! Incorrect Choice.")
                elif chk==7:
                    deleteAcc.delacc(userGivenNumber)
                    break
                elif chk==8:
                    break
                else:
                    print("Oops! Incorrect Choice.")
        else:
            continue
    elif ch==3:
        print("THANK YOU FOR BANKING WITH US")
        break
    else:
        print("Oops! Incorrect Choice.")
