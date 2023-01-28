import random

def captcha():
    u="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    l="abcdefghijklmnopqrstuvwyz"
    n="0123456789012356789012356789"
    all=u+l+n
    len=7
    capt="".join(random.sample(all,len))
    result=''
    for i in capt:
        result=result+'\u0336'+i
    print(result)
    return capt