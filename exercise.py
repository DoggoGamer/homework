def getY(X):
    return X+ 10
    
Res = getY(12)
print(Res)



def getmax(x,y):
    if x > y:
        return x
    else:
        return y


res=getmax(4,8)
print(res)

def GetMaxArrayVer(array):
    currentNum=0
    length_of_array=len(array)
    y= array[0]
    while currentNum != length_of_array:
        x=array[currentNum]
        if x > y:
            y=x
        currentNum=currentNum+1    
    return y

res=GetMaxArrayVer([2,4,3,7,12,5,3])
print(res)