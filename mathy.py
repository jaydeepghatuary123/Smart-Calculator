responses=["Welcome to smart calculator ","My name is Munna ","Thanks",
           "sorry ,this is beyond my ability"]

def extract_numbers_from_text(text):
    l=[]
    for i in text.split(' '):
        try:
            l.append(float(i))

        except ValueError:
            pass
    return l


def lcm(a,b):
    l=a if a>b else b
    while l<=a*b:
        if l%a==0 and l%b==0:
            return l
        l+=1

def hcf(a,b):
    h=a if a<b else b
    while h>=1:
        if a%h==0 and b%h==0:
            return h
        h-=1

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def multiply(a,b):
    return a*b

def division(a,b):
    return a/b

def end():
    print(responses[2])
    input("Press Enter Key to exit")
    exit()

def myname():
    print(responses[1])

def sorry():
    print(responses[3])


operations={"PLUS":add,"ADD":add,"ADDITION":add,"SUM":add,
            "SUBTRACTION":sub,"SUBTRACT":sub,"DIFFERENCE":sub,
            "PRODUCT":multiply,"MULTIPLICATION":multiply,"MULTIPLY":multiply,
            "DIVIDE":division,"DIVISION":division,
            }

commands={"NAME":myname,"END":end,"EXIT":end,"CLOSE":end}































