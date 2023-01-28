import pickle

def uniqueNumberDelete(userGivenNumber):
    uniqueNumber=open('chk.dat','rb')
    lst=[]
    while True:
        try:
            uniqueNumberCheck=pickle.load(uniqueNumber)
            lst.append(uniqueNumberCheck)
        except EOFError:
            break
    uniqueNumber.close()
    uniqueCheck=open('chk.dat','wb')
    for t in lst:
        if t==userGivenNumber:
            continue
        pickle.dump(t, uniqueCheck)
    uniqueCheck.close()
    return 1