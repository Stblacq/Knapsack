def getSwaps(word):
    items = list(word)
    swaps= []
    for i in range(len(items)-1):
        temp = [x for x in items]
        temp[i],temp[i+1]=temp[i+1],temp[i]
        swaps.append(''.join(temp))
    return swaps
        # TODO: write code...
        

print(getSwaps("ABCD"))
