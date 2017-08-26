def intersect(list1,list2):
    temp=[]
    for i in list1:
        if i in list2:
            temp.append(i)
    return temp
def genArraysList(a,b,defaultValue=0): 
    """
    
    returns an matrix of zeroes,size aXb kind of object using lists within a list
    
    """
    try:
        assert a>0,b>0
        temp=[]
        for i in range(a):
            temp.append([defaultValue]*b)
        return temp
    except AssertionError:
        print("invalid Values")
        return -999
#print(genArraysList(5,6))
def printMatrix(l):
    try:
        assert len(l)>0
        for i in l:
            for j in i:
                print(str(j).rjust(10),end="")
            print("\n")
    except AssertionError:
        print("invalid Values")
        return -999