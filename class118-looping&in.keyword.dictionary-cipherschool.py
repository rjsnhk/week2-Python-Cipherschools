
user_info={
    'name':'raj',
    'age':19,
    'movie':['kgf','rrr','mca'],
    'song':['humnava','let me']
}

# # for key present
# if 'name' in user_info:
#     print('present')
# else:
#     print('absent')

# for values present
# if 'raj' in user_info.values():
#     print('value present')
# else:
#     print('absent')

# loops
# for i in user_info:
#     print(i)

# for i in user_info.values():
#     print(i) 

# also for values
# for i in user_info:
#     print(user_info[i])


# v=user_info.values()
# print(v) #out-->dict_values(['raj', 19, ['kgf', 'rrr', 'mca'],['humnava', 'let me']])

# print(type(v))  #out--><class 'dict_values'>

# k=user_info.keys()
# print(k)
# print(type(k))

# item method -- ek ek detail ko list krega
# item=user_info.items()
# print(item)   #out-->dict_items([('name', 'raj'), ('age', 19), ('movie', ['kgf', 'rrr', 'mca']),('song', ['humnava', 'let me'])])

# for i in user_info.items():
#     print(i)

for i,j in user_info.items():
    print(f'key is {i} and value is {j}')  #out--> i=key ,j=value



