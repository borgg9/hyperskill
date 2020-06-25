import random

print("H A N G M A N")
random_guess = random.choice(['python', 'java', 'kotlin', 'javascript'])
random_guess_guion = list(len(random_guess) * "-")
tries = 8
words_used = list()
x = ''

while x != 'play':
    if x == 'exit': exit()
    x = input('Type "play" to play the game, "exit" to quit: ')
while tries > 0 and x == 'play':
    print('')
    print(''.join(random_guess_guion))
    guess = input("Input a letter: ")
    
    if len(guess) != 1: print('You should input a single letter')
    elif not guess.islower(): print('It is not an ASCII lowercase letter')   
    else:
        if guess in random_guess and guess not in words_used:
            words_used.append(guess)
            word = [index for index, element in enumerate(random_guess) if element == guess]
            for i in word:
                random_guess_guion[i] = guess
            if "-" not in random_guess_guion:
                print("You guessed the word\nYou survived!")
                break
        elif guess in words_used: print("You already typed this letter")
        else:
            print("No such letter in the word")
            words_used.append(guess)
            tries -= 1       
    if tries == 0 and "-" in random_guess_guion: print("You are hanged!")
