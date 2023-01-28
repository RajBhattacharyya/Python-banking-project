import pickle

def deleteLoan(lid):
    deleteLoan=open("Loan.dat","rb")
    st=[]
    while True:
        try:
            fin=pickle.load(deleteLoan)
            st.append(fin)
        except EOFError:
            break
    deleteLoan.close()
    fy=open("Loan.dat","wb")
    for i in st:
        if i['Loan id']==lid:
            continue
        pickle.dump(i, fy)
    print("Your Loan has been successfully closed.")
    fy.close()