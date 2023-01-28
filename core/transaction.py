import pickle
import captcha

def trs(userGivenNumber, a):
    fa=open("Banking.dat","rb+")
    sa={}
    fd=False
    try:
        while True:
            c=fa.tell()
            sa=pickle.load(fa)
            if sa['Account no']==userGivenNumber:
                if sa['Acc. Type']=="Savings":
                    if a==1:
                        withdrawAmt=int(input("Enter the amount you want to withdraw: "))
                        choice=1
                    else:
                        ac=input("Enter the Account to which amount to be transfered(Must be more than 6 digits): ")
                        while True:
                            if len(ac)>=6:
                                break
                            else:
                                ac=input("Re-Enter the Account number: (Must contain 6 digit or more)")
                        withdrawAmt=int(input("Enter the amount to be transfered: "))
                        print("To complete Online Transaction please write the Captcha displayed on the screen. \n")
                        res=captcha.captcha()
                        ty=4
                        while ty>0:
                            s=input("\nEnter the captcha displayed: ")
                            if s==res:
                                choice=2
                                break
                            else:
                                ty=ty-1
                                print("Incorrect Captcha. Attempt left ", ty)
                        else:
                            print("Sorry!:( \nYou entered wrong captcha 4 times! \nYour transaction failed:(")
                            choice=0
                    if choice!=0:        
                        while True:
                            if withdrawAmt>0 and withdrawAmt<=sa['Balance']:
                                sa['Balance']=sa['Balance']-withdrawAmt
                                if choice==1:
                                    print("Transaction Successful :)")
                                elif choice==2:
                                    ast=''
                                    for i in range(0, len(ac)-3):
                                        ast=ast+'*'
                                    print("Transaction Successful.... Amount transfered to account", ast+ac[len(ac)-3:])
                                break
                            elif withdrawAmt>0 and withdrawAmt>sa['Balance']:
                                print("Transaction Failed :( \nInsufficient Balance....")
                                break
                            else:
                                withdrawAmt=int(input("Re-Enter the amount: "))
                    else:
                        break
                else:
                    print("This is FD account... You can not withdraw your money...")
                fa.seek(c)
                pickle.dump(sa, fa)
                fd=True
    except EOFError:
        if fd==False:
            print("Transaction Failed")
        else:
            print("Your current balance is", sa['Balance'])
        fa.close()