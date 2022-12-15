l1=[1,2,3,4,5]
l2=[1,2,3,4,6,7]
out=[]
def common(l1,l2):
    for i in l1:
        if i in l2:
            out.append(i)
    return out
print(common(l1,l2))