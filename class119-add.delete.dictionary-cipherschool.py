user_info={
    'name':'raj',
    'age':19,
    'movie':['kgf','rrr','mca'],
    'song':['humnava','let me']
}

# # add data
# user_info['music']=['song1','song2']
# print(user_info)  #out-->{'name': 'raj', 'age': 19, 'movie': ['kgf', 'rrr', 'mca'], 'song': ['humnava', 'let me'],'music': ['song1', 'song2']}

# pop method for delete
# popped_item=user_info.pop('age')
# print(user_info)
# print(popped_item)


#popitem method -- last wala random delete hoga
popped_item=user_info.popitem()
print(popped_item)  
print(type(popped_item))  #tuple
print(user_info)

