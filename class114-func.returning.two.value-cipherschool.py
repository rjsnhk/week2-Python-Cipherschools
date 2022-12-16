# func return two values
def func(int1,int2):
    add=int1+int2
    multi=int1*int2
    return add,multi
# print(func(2,3))  #output(5, 6) it gives as tuple
add,multi=func(2,3)
print(add)   #5
print(multi)    #6
