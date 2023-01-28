import pickle

def userAccNumberCheck(userUniqueNumber):
    uniqueNumber=open('chk.dat','rb')
    lst=[]
    while True:
        try:
            uniqueNumberCheck=pickle.load(uniqueNumber)
            lst.append(uniqueNumberCheck)
        except EOFError:
            break
    uniqueNumber.close()
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
    uniqueCheck=open('chk.dat','wb')
    for t in lst:
        pickle.dump(t, uniqueCheck)
    uniqueCheck.close()
    return userUniqueNumber