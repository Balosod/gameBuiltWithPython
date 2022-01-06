from random import shuffle
mylist=[' ', 'O', ' ']
def shuffle_list (mylist):
    
    '''
    by calling this function the index position of "O" is going to 
    be change between index 0,1 and 2
    '''
    
    shuffle(mylist)
    return mylist


def guess_index ():
    
    '''
    calling this function allow the player to input a number between 0,1,2 
    and if the number is not between this 3 numbers, the loop continue to run
    '''
    guess = []
    while guess not in  ['0','1','2']:
        
            guess=input('Enter 0 or 1 or 2: ')
            
    return int(guess)

def check(mylist,guess):
    
    '''
     This function compare the player input to the actual index position of 'O' in mylist
     if equal it will print CORRECT GUESS and if not it will print WRONG GUESS
    '''
    if mylist[guess] == 'O':
        print('CORRECT GUESS')
    else:
        print('WRONG GUESS')

print("WELCOME TO GUESS ME!")
print("There are there black boxes, and a ball was place in one of the there boxes")
print("Pick 0, 1 or 2 to choose the box that contain the ball")
print("LET'S PLAY!")
# shuffle the list
rearrange_list = shuffle_list(mylist)

# guess a number
player_guess = guess_index()

# check 
check(rearrange_list, player_guess)
