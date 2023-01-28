import datetime
from dateutil import relativedelta
import password
import random
import userAccount
import pickle

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
    transactionPassword=password.passd()
    userUniqueNumber=random.randint(10000,99999)
    userAccountNumber=userAccount.userAccNumberCheck(userUniqueNumber)
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