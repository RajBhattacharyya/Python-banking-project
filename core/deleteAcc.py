import pickle
import uniqueDelete

def delacc(userGivenNumber):
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
                if i['Account no']==userGivenNumber:
                    continue
                pickle.dump(i, fa)
            co=uniqueDelete.uniqueNumberDelete(userGivenNumber)
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