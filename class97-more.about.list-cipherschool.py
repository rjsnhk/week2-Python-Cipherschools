# # generate list with range functions
# number=list(range(1,11))
# # print(number)


number=[4,1,2,3,10,4,5,1,5,6]
# number.pop()
# print(number)
# print(number.pop())

# to find position
# print(number.index(10))  #3rd
# print(number.index(1))  #1 not 7

# 1=find number , 2=start from ,6=end
# print(number.index(1,2,8))  #1 not 7 


def neg_list(l):
    negative=[]
    for i in l:
        negative.append(-i)
    return negative
print(neg_list(number))



