
def Vector(n):
    l=[]
    for i in range(0,n):
        l.append([])
        l[i]=[]
    return l

def Matrix(m,n):
    mt=[]
    for i in range(0,m):
        mt.append(Vector(n))
    return mt


