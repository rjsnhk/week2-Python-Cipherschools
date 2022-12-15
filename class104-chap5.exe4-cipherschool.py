a=[1,2,3,4,5,6,7]
odd=[]
even=[]
def test(l):
    for i in l:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    output=[odd,even]
    return output
print(test(a))

# out put ==[[1, 3, 5, 7], [2, 4, 6]]