def greater(a,b):
    if a>b:
        return a
    else:
        return b
    
def greatest(a,b,c):
    return greater(greater(a,b),c)

print(greatest(0,9,34))