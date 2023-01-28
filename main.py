import pickle
import random
import stdiomask
import datetime
from dateutil import relativedelta
def new(userAccountChoice):
    user={}
    fileHandle=open("Banking.dat","ab")
    userName=input("Enter Name: ")
    dob=input("Enter Date of birth (YYYY/MM/DD): ")
    while True:
        try:
            userDOB=datetime.datetime.strptime(dob, "%Y/%m/%d").date()
            today=datetime.date.today()
            year=relativedelta.relativedelta(today, userDOB)
            userAge=year.years
            if userAge>=18:
                break
            else:
                dob=input("Re-Enter Date of birth(Must be above 18 years of age) (YYYY/MM/DD): ") 
        except ValueError:
            print("Incorrect date format")
            dob=input("Re-Enter Date of birth (YYYY/MM/DD): ")
    gender=input("Enter your Gender (M/F/T): ")
    while True:
        if gender.upper()=='M' or gender.upper()=='F' or gender.upper()=='T':
            break
        else:
            gender=input("Re-Enter your Gender (M/F/T): ")
    aadhaarNumber=int(input("Enter your 12-digit Aadhaar No.: "))
    while True:
        if aadhaarNumber in range(100000000000, 1000000000000):
            break
        else:
            aadhaarNumber=int(input("Re-enter your Aadhaar No.(Must contain 12-digits): "))
    address=input("Enter your Address: ")
    phoneNumber=int(input("Enter your 10-digit Mobile no.: "))
    while True:
        if phoneNumber in range(1000000000, 10000000000):
            break
        else:
            phoneNumber=int(input("Re-enter your Mobile No.(Must contain 10-digits): "))
    email=input("Enter your Email id.: ")
    occupation=input("Enter your Occupation: ")
    salary=int(input("Enter your Salary: "))
    transactionPassword=passd()
    userUniqueNumber=random.randint(10000,99999)
    userAccountNumber=userAccNumberCheck(userUniqueNumber)
    bal=0
    loan="Nil"
    if userAccountChoice==1:
        user['Acc. Type']="Savings"
    elif userAccountChoice==2:
        user['Acc. Type']="Fixed 5yrs"
    elif userAccountChoice==3:
        user['Acc. Type']="Fixed 7yrs"
    else:
        user['Acc. Type']="Fixed 10yrs"
    user['Account no']=userAccountNumber
    user['User Name']=userName
    user['D-o-B ']=userDOB
    user['Gender']=gender
    user['Aadhaar No.']=aadhaarNumber
    user['Address']=address
    user['Mobile No.']=phoneNumber
    user['Email']=email
    user['Occupation']=occupation
    user['Salary']=salary
    user['Balance']=bal
    user['Transaction Password']=transactionPassword
    user['Active loan']=loan
    pickle.dump(user, fileHandle)
    print("_._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._ \nAccount creation successful. \n----------------------------\nYour account number is: ", userAccountNumber, "\n=======================")
    fileHandle.close()
def passd():
    transactionPassword=stdiomask.getpass("Enter Transaction Password(Must contain atleast 8 characters with symbols & numbers): ")
    while True:
        ct=0
        count=0
        count1=0
        count2=0
        count3=0
        count4=0
        for i in transactionPassword:
            if i.islower():
                count+=1
                ct+=1
            elif i.isupper():
                count1+=1
                ct+=1
            elif i.isdigit():
                count2+=1
                ct+=1
            elif i.isspace():
                count3+=1
            else:
                count4+=1
                ct+=1
        if ct>=8 and count3==0:
            if count>=1:
                if count1>=1:
                    if count2>=1:
                        if count4>=1:
                            break
                        else:
                            print("Weak password. \nTry including special characters.")
                            transactionPassword = stdiomask.getpass("Re-Enter Transaction Password: ")
                    else:
                        print("Weak password. \nTry including numericals.")
                        transactionPassword = stdiomask.getpass("Re-Enter Transaction Password: ")
                else:
                    print("Weak password. \nTry including upper case alphabets.")
                    transactionPassword = stdiomask.getpass("Re-Enter Transaction Password: ")
            else:
                print("Weak password. \nTry including lower case alphabets.")
                transactionPassword = stdiomask.getpass("Re-Enter Transaction Password: ")
        elif ct>=8 and count3!=0:
            transactionPassword = stdiomask.getpass("Re-Enter Transaction Password(Must not contain any spaces): ")
        elif ct<8:
            transactionPassword = stdiomask.getpass("Re-Enter Transaction Password(Must contain 8 characters): ")
    return transactionPassword
def userAccNumberCheck(userUniqueNumber):
    un=open('chk.dat','rb')
    lst=[]
    while True:
        try:
            unk=pickle.load(un)
            lst.append(unk)
        except EOFError:
            break
    un.close()
    if userUniqueNumber in lst:
        while True:
            userUniqueNumber=random.randint(1,9)
            if userUniqueNumber in lst:
                continue
            if userUniqueNumber not in lst:
                lst.append(userUniqueNumber)
                break
    else:
        lst.append(userUniqueNumber)
    uk=open('chk.dat','wb')
    for t in lst:
        pickle.dump(t, uk)
    uk.close()
    return userUniqueNumber
def check(sk):
    fc=open("Banking.dat","rb")
    std={}
    found=False
    ty=4
    try:
        while True:
            std=pickle.load(fc)
            if std['Account no']==sk:
                while ty>0:
                    passd=stdiomask.getpass("Enter your account password: ")
                    if std['Transaction Password']==passd:
                        print("Account Found.")
                        global fd
                        fd=1
                        return fd
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
        fc.close()
    return fd
def details(sk):
    fc=open("Banking.dat","rb")
    sta={}
    try:
        while True:
            sta=pickle.load(fc)
            if sta['Account no']==sk:
                for key,value in sta.items():
                    if key=="Transaction Password":
                        continue
                    else:
                        print('||', key,'\t|', value)
    except EOFError:
        fc.close()
def modify(sk, m):
    fx=open("Banking.dat","rb+")
    sd={}
    fd=False
    try:
        while True:
            a=fx.tell()
            sd=pickle.load(fx)
            if sd['Account no']==sk:
                if m==1:
                    k=input("Enter new User Name: ")
                    sd['User Name']=k
                elif m==2:
                    k=input("Enter new Date of Birth(YYYY/MM/DD): ")
                    while True:
                        try:
                            userDOB=datetime.datetime.strptime(k, "%Y/%m/%d").date()
                            break
                        except ValueError:
                            print("Incorrect date format")
                            k=input("Re-Enter Date of birth (YYYY/MM/DD): ")
                    sd['D-o-B ']=userDOB
                elif m==3:
                    k=int(input("Enter new Aadhaar No.: "))
                    while True:
                        if k in range(100000000000, 1000000000000):
                            break
                        else:
                            k=int(input("Re-enter your Aadhaar No.(Must contain 12-digits): "))
                    sd['Aadhaar No.']=k
                elif m==4:
                    k=int(input("Enter new Mobile no.: "))
                    while True:
                        if k in range(1000000000, 10000000000):
                            break
                        else:
                            k=int(input("Re-enter your Mobile No.(Must contain 10-digits): "))
                    sd['Mobile No.']=k
                elif m==5:
                    k=input("Enter new Email: ")
                    sd['Email']=k
                elif m==6:
                    k=input("Enter new Occupation: ")
                    sd['Occupation']=k
                elif m==7:
                    k=int(input("Enter new Salary: "))
                    sd['Salary']=k
                else:
                    k=passd()
                    sd['Transaction Password']=k
                fx.seek(a)
                pickle.dump(sd,fx)
                fd=True
    except EOFError:
        if fd==False:
            print("Updation Fail")
        else:
            print("Updation Successful")
        fx.close()
def deposit(sk, k):
    ft=open("Banking.dat","rb+")
    sd={}
    fd=False
    try:
        while True:
            b = ft.tell()
            sg = pickle.load(ft)
            if sg['Account no']==sk:
                if k==1:
                    dp=int(input("Enter the amount you want to deposit: "))
                    while True:
                        if dp>0:
                            sg['Balance']=sg['Balance']+dp
                            break
                        else:
                            dp=int(input("Re-Enter the amount you want to deposit: "))
                else:
                    cq=int(input("Enter cheque number: "))
                    dp=int(input("Enter the amount of the cheque: "))
                    while True:
                        if dp>0:
                            sg['Balance']=sg['Balance']+dp
                            print("Your cheque of number", cq, "is processing...... \nPlease wait.... ... .. . .")
                            break
                        else:
                            dp=int(input("Re-Enter the amount: "))
                ft.seek(b)
                pickle.dump(sg, ft)
                fd=True
    except EOFError:
        if fd==False:
            print("Transaction Failed")
        else:
            print("Tansaction Successful. \nYour current balance is", sg['Balance'])
        ft.close()
def captcha():
    u="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    n="0123456789012356789012356789"
    all=u+u+n
    len=6
    capt="".join(random.sample(all,len))
    result=''
    for i in capt:
        result=result+'\u0336'+i
    print(result)
    return capt
def trs(sk, a):
    fa=open("Banking.dat","rb+")
    sa={}
    fd=False
    try:
        while True:
            c=fa.tell()
            sa=pickle.load(fa)
            if sa['Account no']==sk:
                if sa['Acc. Type']=="Savings":
                    if a==1:
                        wt=int(input("Enter the amount you want to withdraw: "))
                        ch=1
                    else:
                        ac=input("Enter the Account to which amount to be transfered(Must be more than 6 digits): ")
                        while True:
                            if len(ac)>=6:
                                break
                            else:
                                ac=input("Re-Enter the Account number: (Must contain 6 digit or more)")
                        wt=int(input("Enter the amount to be transfered: "))
                        print("To complete Online Transaction please write the Captcha displayed on the screen. \n")
                        res=captcha()
                        ty=4
                        while ty>0:
                            s=input("\nEnter the captcha displayed: ")
                            if s==res:
                                ch=2
                                break
                            else:
                                ty=ty-1
                                print("Incorrect Captcha. Attempt left ", ty)
                        else:
                            print("Sorry!:( \nYou entered wrong captcha 4 times! \nYour transaction failed:(")
                            ch=0
                    if ch!=0:        
                        while True:
                            if wt>0 and wt<=sa['Balance']:
                                sa['Balance']=sa['Balance']-wt
                                if ch==1:
                                    print("Transaction Successful :)")
                                elif ch==2:
                                    ast=''
                                    for i in range(0, len(ac)-3):
                                        ast=ast+'*'
                                    print("Transaction Successful.... Amount transfered to account", ast+ac[len(ac)-3:])
                                break
                            elif wt>0 and wt>sa['Balance']:
                                print("Transaction Failed :( \nInsufficient Balance....")
                                break
                            else:
                                wt=int(input("Re-Enter the amount: "))
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
def loanchk(sk):
    fac=open("Banking.dat","rb")
    sta={}
    try:
        while True:
            sta=pickle.load(fac)
            if sta['Account no']==sk:
                if sta['Active loan']=='Nil':
                    print("You do not have any active loan therefore you can apply for a loan. \nMinimum salary required is 25000/-")
                    while True:
                        con=input("Do you want to continue? (Y/N): ")
                        print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
                        if con.upper()=="Y":
                            if sta['Salary']>=25000:
                                print("You are eligilbe for a loan.....")
                                ln=0
                                break
                            else:
                                ln=1
                                break
                        elif con.upper()=="N":
                            ln=3
                            break
                        else:
                            continue
                else:
                    ln=2
    except EOFError:
        fac.close()
    return ln
def loannew(sk):
    ln=loanchk(sk)
    if ln==2:
        print("You already have an active loan. \nBefore you take a new loan you must repay your old loan")
    elif ln==1:
        print("Your income is less than the required income necessary for loan. \nSorry you are not eligible for loan")
    elif ln==0:   
        lnn={}
        print("Our Bank provide loan at very low interest rates. \n============================================ \nWe provide different kinds of loan. \n1. Home Loan \n2. Car Loan \n3. Business Loan \n4. Education Loan \n5. Personal Loan")
        while True:
            chl=int(input("Enter 1, 2, 3, 4, 5: "))
            print("--.--.--.--.--.--.--")
            if chl==1:
                lt="Home Loan"
                print("We provide home loan @6.65 p.a")
                li=6.65
                break
            elif chl==2:
                lt="Car Loan"
                print("We provide car loan @7.70 p.a")
                li=7.70
                break
            elif chl==3:
                lt="Business Loan"
                print("We provide Business loan @11.10 p.a")
                li=11.10
                break
            elif chl==4:
                lt="Education Loan"
                print("We provide education loan @9.15 p.a")
                li=9.15
                break
            elif chl==5:
                lt="Personal Loan"
                print("We provide personal loan @9.60 p.a")
                li=9.60
                break
            else:
                print("You entered wrong input.")
                continue
        while True:
            la=int(input("Enter Loan Amount (Minimum 100000): "))
            if la>=100000:
                break
            else:
                continue
        while True:
            print("We provide loan for 4-20 yrs")
            ly=int(input("Enter the time period for your loan(4-20): "))
            if ly>=4 and ly<=20:
                break
            else:
                continue
        col=input("Enter the details of your collateral: ")
        gar=input("Enter the name of your guarantor(If the person dies the guarantor will pay the loan): ")
        tamt=int(la*(pow((1 + li/100), ly)))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        while True:
            conf=input("Do you want to continue? (Y/N): ")
            if conf.upper()=="Y":
                lid=random.randint(1,1000000)
                fth=open("Loan.dat","ab")
                lnn['Loan id']=lid
                lnn['User Name']=sk
                lnn['Loan Type']=lt
                lnn['Loan Amount']=la
                lnn['Loan Period']=ly
                lnn['Interest']=li
                lnn['Total Amt']=tamt
                lnn['Col Details']=col
                lnn['Guarantor']=gar
                pickle.dump(lnn, fth)
                fth.close()
                alo="Yes"
                fg=open("Banking.dat","rb+")
                sd={}
                try:
                    while True:
                        d=fg.tell()
                        sd=pickle.load(fg)
                        if sd['Account no']==sk:
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
def loandel(lid):
    fc=open("Loan.dat","rb")
    ld={}
    try:
        while True:
            ld=pickle.load(fc)
            if ld['Loan id']==lid:
                for key,value in ld.items():
                    print('||', key, '\t|', value)
    except EOFError:
        fc.close()
def dell(lid):
    dell=open("Loan.dat","rb")
    st=[]
    while True:
        try:
            fin=pickle.load(dell)
            st.append(fin)
        except EOFError:
            break
    dell.close()
    fy=open("Loan.dat","wb")
    for i in st:
        if i['Loan id']==lid:
            continue
        pickle.dump(i, fy)
    print("Your Loan has been successfully closed.")
    fy.close()
def loandep(lid, sk):
    ft=open("Loan.dat","rb")
    sd={}
    amtl=0
    try:
        while True:
            sg = pickle.load(ft)
            if sg['Loan id']==lid:
                amtl=sg['Total Amt']
    except EOFError:
        ft.close()
    print("Amount left to repay the loan ", amtl)
    dp=int(input("Enter the amount you want to repay: "))
    while True:
        if dp>0:
            if dp<amtl:
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
            elif dp==amtl:
                dell(lid)
                fg=open("Banking.dat","rb+")
                sd={}
                try:
                    while True:
                        d=fg.tell()
                        sd=pickle.load(fg)
                        if sd['Account no']==sk:
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
def unodell(sk):
    un=open('chk.dat','rb')
    lst=[]
    while True:
        try:
            unk=pickle.load(un)
            lst.append(unk)
        except EOFError:
            break
    un.close()
    uk=open('chk.dat','wb')
    for t in lst:
        if t==sk:
            continue
        pickle.dump(t, uk)
    uk.close()
    return 1
def delacc(sk):
    fd=open("Banking.dat","rb")
    st=[]
    while True:
        try:
            fin=pickle.load(fd)
            st.append(fin)
        except EOFError:
            break
    fd.close()
    print("Are you sure you want to close your Account:")
    while True:
        ch=input("Confirm/Exit: ")
        if ch.lower()=="confirm":
            fa=open("Banking.dat","wb")
            for i in st:
                if i['Account no']==sk:
                    continue
                pickle.dump(i, fa)
            co=unodell(sk)
            if co==1:
                print("Your Account has been successfully closed.")
            else:
                print("Account can not be closed.")
            fa.close()
            break
        elif ch.lower()=="exit":
            break
        else:
            continue
                    
print("\t\t\t\t*********************************** \n\t\t\t\t(: WELCOME TO OUR BANKING SYSTEM :) \n\t\t\t\t***********************************")
while True:
    print("1. Create an account \n2. Existing User \n3. Exit")
    ch=int(input("Enter 1, 2 or 3: "))
    if ch==1:
        print("~~~~~~~~~~~~~~~~~~~~~~ \nSelect an Account type: \n1. Saving \n2. Fixed")
        userAccountChoice=int(input("Choose 1 or 2: "))
        if userAccountChoice==1:
            print("---------------- \nThanking for choosing a Saving account....... \nYou will be getting an interest of 3.5% p.a \nPlease complete the following procedure to create an account. \n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            new(userAccountChoice)
        elif userAccountChoice==2:
            print("------------------ \nThanking for choosing a Fixed account......... \nOur bank provide you with 3 different kind of FD accounts:- \nFD for 5 years @ 7.5% p.a \nFD for 7 years @ 9% p.a \nFD for 10 years @ 12% p.a")
            ten=int(input("Enter a tenure for your Fixed account: (5, 7 or 10): "))
            ed="Please complete the following procedure to create an account. \n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
            if ten==5:
                print("You will be getting an interest of 7.5% p.a \n", ed)
                userAccountChoice=2
                new(userAccountChoice)
            elif ten==7:
                print("You will be getting an interest of 9% p.a \n", ed)
                userAccountChoice=3
                new(userAccountChoice)
            elif ten==10:
                print("You will be getting an interest of 12% p.a \n", ed)
                userAccountChoice=4
                new(userAccountChoice)
            else:
                print("Oops! Incorrect Choice.")
        else:
            print("Oops! Incorrect Choice.")
    elif ch==2:
        print("--------------------")
        sk=int(input("Enter account number: "))
        fd=0
        check(sk)
        if fd==1:
            while True:
                print("~~~~~~~~~~~~~~ \nWhat do you want to do? \n1. Check your account details \n2. Modify your account details \n3. Deposit Money \n4. Withdraw Money \n5. Online Transaction \n6. Loan \n7. Delete Account \n8. Back")
                chk=int(input("Enter 1, 2, 3, 4, 5, 6, 7 or 8: "))
                print("-----------------------------")
                if chk==1:
                    details(sk)
                elif chk==2:
                    print("What do you want to modify? \n1. Name \n2. Date of Birth \n3. Aadhaar Number \n4. Mobile No. \n5. Email \n6. Occupation \n7. Salary \n8. Transaction Password \n9. Back") 
                    m=int(input("Choose an Option to modify(1-9): "))
                    if m in range(1, 9):
                        modify(sk, m)
                    elif m==9:
                        continue
                    else:
                        print("Oops! Incorrect Choice.")
                elif chk==3:
                    print("Choose a method for deposting money: \n1. Cash \n2. Cheque \n3. Back")
                    k=int(input("Enter 1, 2 or 3: "))
                    print("~~~~~~~~~~~~~~~")
                    if k==1 or k==2:
                        deposit(sk, k)
                    elif k==3:
                        continue
                    else:
                        print("Oops! Incorrect Choice.")
                elif chk==4:
                    a=1
                    trs(sk, a)
                elif chk==5:
                    a=2
                    trs(sk, a)
                elif chk==6:
                    print("(:Welcome to our loan service:) \n1. New loan \n2. Existing loan \n3. Back")
                    ka=int(input("Enter 1, 2 or 3: "))
                    print("~~~~~~~~~~~")
                    if ka==1:
                        loannew(sk)
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
                                    loandel(lid)
                                elif cho==2:
                                    loandep(lid, sk)
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
                    delacc(sk)
                    break
                elif chk==8:
                    break
                else:
                    print("Oops! Incorrect Choice.")
        else:
            break
    elif ch==3:
        print("THANK YOU FOR BANKING WITH US")
        break
    else:
        print("Oops! Incorrect Choice.")
