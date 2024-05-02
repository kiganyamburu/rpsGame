import random, sys

print('ROCK, PAPER, SCISSORS')

# variables that keep track of the number of the number of wins, looses and ties
wins = 0
looses = 0
ties = 0

while True: # the main loop
    print('%s wins, %s losses, %s ties' % (wins,looses, ties))
    while True: # The player input loop
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit()
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break
        print('Type r, p, s or q.')
        
        
    # what players chose 
    if playerMove == 'r':
        print('ROCK verse.....')
    elif playerMove == 'p':
        print('PAPER verse.....')
    elif playerMove == 's':
        print('SCISSORS verse.....')
        
        
    # what computer chose
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = 'r'
        print('ROCK')
    elif randomNumber == 2:
        computerMove = 'p'
        print('PAPER')
    elif randomNumber == 3:
        computerMove = 's'
        print('SCISSORS')
        
    # Displays and record the wins/losses/ties 
    if playerMove == computerMove:
        print('Its a tie')
        ties = ties + 1
    elif playerMove == 'r' and computerMove == 's':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'r':
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'r' and computerMove == 'p':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 's':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 's' and computerMove == 'r':
        print('You lose!')
        losses = losses + 1
        
        