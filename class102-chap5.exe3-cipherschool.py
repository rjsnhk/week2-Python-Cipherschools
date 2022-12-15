a=['abc','def','ced']
b=[]
def rev(l):
    for i in l:
        b.append(i[::-1])
    return (b)
print(rev(a))