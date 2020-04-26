import random
def genEven():
    random_number = random.randint(0,99)
    
    if random_number % 2 == 0:
      return random_number
    else:
      return genEven()


# dist = [genEven() for x in range(100)]
# print(dist)

def toStr(n,base):
   convertString = "0123456789ABCDEF"
   if n < base:
      return convertString[n]
   else:
      return toStr(n//base,base) + convertString[n%base]

def strToDec(str):
    dec ={"A":10,"B":11,"C":12,"D":13,"E":14,"F":15}
    try:
        return dec[str]
    except:
        return int(str)
   


def getSampleSpaceOfNsidesDice(N,rolls):
        space = []
        for i in range((N+1)**rolls):
            combo_string = toStr(i,(N+1)).zfill(rolls)
            combo = list(combo_string)
            if '0' not in combo:
                space.append(combo)
                print (combo)
        return space

space = getSampleSpaceOfNsidesDice(8,3)
count = 0
for x in space:
    if strToDec(x[0])== strToDec(x[1])==strToDec(x[2]):
        count +=1
print(count)
