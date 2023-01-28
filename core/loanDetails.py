import pickle

def loandel(lid):
    fileOpen=open("Loan.dat","rb")
    ld={}
    try:
        while True:
            ld=pickle.load(fileOpen)
            if ld['Loan id']==lid:
                for key,value in ld.items():
                    print('||', key, '\t|', value)
    except EOFError:
        fileOpen.close()