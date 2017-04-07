def sign(n):
    if n>0:
        return 1
    return -1

def innerProduct(w,x):
    DimensionOfData=length(x)
    result=0
    for n in range(0,DimensionOfData):
        result+=w[n]*x[n]
    return result

def shouldHalt(w,x,y):
    lengthOfData=length(x)
    for n in range(0,lengthOfData):
        if sign(innerProduct(w,x))!=y:
            return 0
    return 1

w=[0,0,0,0,0]

