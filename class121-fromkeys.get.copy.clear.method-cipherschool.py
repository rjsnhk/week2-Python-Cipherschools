# fromkeys
# output like -- d={'name':'unknown','age':'unknown'}

# d=dict.fromkeys(['name','age'],'unknown')
# print(d) #out=={'name': 'unknown', 'age': 'unknown'}

# d=dict.fromkeys(('name','age'),'unknown')
# print(d)

# d=dict.fromkeys("abc",'unknown')
# print(d) #out--{'a': 'unknown', 'b': 'unknown', 'c': 'unknown'}

# d=dict.fromkeys(range(1,10),'unknown')
# print(d)  #out--{1: 'unknown', 2: 'unknown', 3: 'unknown', 4:'unknown', 5: 'unknown', 6: 'unknown', 7: 'unknown', 8: 'unknown', 9: 'unknown'}

# get method
d={'name': 'unknown', 'age': 'unknown'}
# print(d['names']) error --names no in key for that we use get it

# print(d.get('name')) #unknown
# print(d.get('names')) #none --not error


# if 'names' in d:
#     print('present')
# else:
#     print('not')

# get use if 
# # if d.get('name'):
# #     print('present')
# # else:
# #     print('not')


# # clear method
# d.clear()
# print(d)


# copy method--yha cop alag variable he
# cop=d.copy()
# print(cop.popitem())
# print(cop)
# print(d)
# print(cop is d)  #false


# # ese me equal to hoga but dono ek hi variable hoga pop kre to dono se udega
# d1=d
# print(d1.popitem())
# print(d1)
# print(d)
# print(d1 is d)  #true
