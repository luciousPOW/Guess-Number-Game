attempt = 1
print('Welcome to Guess the Number game')
print()
answer = input('Are you ready to play? ').lower()
if answer == 'yes':
        print("Let's start!")
else:
        print('Awww, Bye :((')
        exit()
while True:
    
        correctGuess = 1500
        print()
        print('Select a number between 1 to 5000')    
        userGuess = int(input('> '))
        if userGuess > correctGuess:
            print('Lower your number')
            attempt += 1
        elif userGuess < correctGuess:
            print('Higher your number')
            attempt += 1
        elif userGuess == correctGuess:
            print('You nailed it!')
            print(f"It took you {attempt} attempt.")
            break
        else:
            print("Can't recognize your number")