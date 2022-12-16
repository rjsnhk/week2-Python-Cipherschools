a=[1,2,[2,3],[3,4],[4,5],4,5,[6,4],[9,4]]
c=[]
def test(l):
    for i in l:
        if type(i)==list:
            c.append(i)
    return len(c)
print(test(a))