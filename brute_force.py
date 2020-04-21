def toStr(n,base):
   convertString = "0123456789ABCDEF"
   if n < base:
      return convertString[n]
   else:
      return toStr(n//base,base) + convertString[n%base]



def yieldAllCombos(items):
        N = len(items)
        for i in range(3**N):
            combo_string = toStr(i,3).zfill(N)
            combo = list(combo_string)
            bag1=[]
            bag2=[]
            for idx, val in enumerate(combo):
                if val == "1":
                    bag1.append(items[idx])
                if val == "2":
                    bag2.append(items[idx])
            yield((bag1,bag2))

yieldAllCombos(["A","B","C","D"])
