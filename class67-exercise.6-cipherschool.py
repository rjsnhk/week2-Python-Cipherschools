# modify number guessing
winning_number=43
guess=1
number=int(input('guess a num between 1 and 100 : '))
game_over=False
while not game_over:
    if number==winning_number:
        print(f'you win and you guess{guess} times')
        game_over=True
    else:
        if number<winning_number:
            print('very low')
            guess+=1
            number=int(input('guess again : '))
        else:
            print('very high')
            guess+=1
            number=int(input('guess again : '))

