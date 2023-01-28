import stdiomask
import random

def passd():
    transactionPassword=stdiomask.getpass("Enter Transaction Password(Must contain atleast 8 characters with symbols & numbers): ")
    while True:
        passwdCheck=0
        count=0
        count1=0
        count2=0
        count3=0
        count4=0
        for i in transactionPassword:
            if i.islower():
                count+=1
                passwdCheck+=1
            elif i.isupper():
                count1+=1
                passwdCheck+=1
            elif i.isdigit():
                count2+=1
                passwdCheck+=1
            elif i.isspace():
                count3+=1
            else:
                count4+=1
                passwdCheck+=1
        if passwdCheck>=8 and count3==0:
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
        elif passwdCheck>=8 and count3!=0:
            transactionPassword = stdiomask.getpass("Re-Enter Transaction Password(Must not contain any spaces): ")
        elif passwdCheck<8:
            transactionPassword = stdiomask.getpass("Re-Enter Transaction Password(Must contain 8 characters): ")
    confirmPassword = stdiomask.getpass("Please confirm your Password: ")
    while True:
        if confirmPassword==transactionPassword:
            return transactionPassword
            break
        else:
            confirmPassword = stdiomask.getpass("Re-enter the Password: ")