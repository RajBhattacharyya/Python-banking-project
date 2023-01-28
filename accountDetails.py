import pickle

def details(userGivenNumber):
    fileOpen=open("Banking.dat","rb")
    sta={}
    try:
        while True:
            sta=pickle.load(fileOpen)
            if sta['Account no']==userGivenNumber:
                for key,value in sta.items():
                    if key=="Transaction Password":
                        continue
                    else:
                        print('||', key,'\t|', value)
    except EOFError:
        fileOpen.close()