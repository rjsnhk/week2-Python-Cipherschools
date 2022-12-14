# a=list(range(1,5))
a=['a','b','c']
# def rev_list(l):
#         return l[::-1]
# print(rev_list(a))


# def rev_list(l):
#         l.reverse()
#         return l
            
# print(rev_list(a))


def rev_list(l):
    str=[]
    for i in range(len(l)):
        poped=l.pop()
        str.append(poped)
    return str
print(rev_list(a))


