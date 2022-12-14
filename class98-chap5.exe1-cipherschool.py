a=list(range(1,10))
square=[]
def sqr_num(l):
    for i in l:
        square.append(i**2)
    return square
print(sqr_num(a))