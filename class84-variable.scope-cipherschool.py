# def func():
#     x=7  #local variable
#     return x
# def func2():
#     print(x)
# func2()  no out put


# x=5  #global
# def func():
#     x=7  #local variable
#     return x
# print(x)
# print(func())



x=5  #global
def func():
    global x #local ko global karta he 
    x=7  #local variable
    return x
print(x)  
print(func())  #func ke niche wala sabhi x local variable bn jaega
print(x)
#output 577