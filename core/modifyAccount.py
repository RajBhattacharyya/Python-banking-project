import datetime
from dateutil import relativedelta
import pickle
import password

def modify(userGivenNumber, m):
    fx=open("Banking.dat","rb+")
    sd={}
    fd=False
    try:
        while True:
            a=fx.tell()
            sd=pickle.load(fx)
            if sd['Account no']==userGivenNumber:
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
                    k=password.passd()
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