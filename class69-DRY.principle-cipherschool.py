# modify number guessing type 2
# winning_number=43
# guess=1
# number=int(input('guess a num between 1 and 100 : '))
# game_over=False
# while not game_over:
#     if number==winning_number:
#         print(f'you win and you guess{guess} times')
#         game_over=True
#     else:
#         if number<winning_number:
#             print('very low')
            
#         else:
#             print('very high')
#         guess+=1
#         number=int(input('guess again : '))


# modify number guessing type 3
# winning_number=43
# guess=1
# while True:
#     number=int(input('guess a num between 1 and 100 : '))
#     if number==winning_number:
#         print(f'you win and you guess{guess} times')
#         break
#     else:
#         if number<winning_number:
#             print('very low')
            
#         else:
#             print('very high')
#         guess+=1
#         continue
    
    
    # modify number guessing type random number
import random
winning_number=random.randint(1,100)
guess=1
while True:
    number=int(input('guess a num between 1 and 100 : '))
    if number==winning_number:
        print(f'you win and you guess{guess} times')
        break
    else:
        if number<winning_number:
            print('very low')
            
        else:
            print('very high')
        guess+=1
        continue