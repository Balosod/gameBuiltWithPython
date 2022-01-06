from random import randint
guess =[0]
value=randint(1,100)
print("WELCOME TO GUESS ME!")
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")

while True:
        guessnum = int(input('Enter a num to guess: '))
        if guessnum < 1 or guessnum > 100 :
            print('OUT OF BOUNDS! try Again')
            continue
       
        if guessnum == value:
            print(f'you guess correctly and you guess {len(guess)} times')
            break
            
        guess.append(guessnum)

        if guess[-2]:  
                if abs(value-guessnum) < abs(value-guess[-2]):
                    print('WARMER!')
                else:
                    print('COLDER!')

        else:
                if abs(value-guessnum) <= 10:
                    print('WARM!')
                else:
                    print('COLD!')
