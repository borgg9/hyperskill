import random

# Write your code here
print("""H A N G M A N\n""")

palabras = ['python', 'java', 'kotlin', 'javascript']
adivinar_word = random.sample(palabras, 1)

# words that are in adivinar_word
opciones_si =[]
# print adivinar_word with ----
adivinar_word_guion = ('-' * ( int(len(adivinar_word))))
# bucle game: 
for ocasion in range(8):
    #1º print the hidden word and ask for a letter
    print('\n' + adivinar_word_guion)
    letra_propuesta = input('Input a letter: ')
    #2º check if letra_propuesta has been said before
    if letra_propuesta in opciones_si:
        continue  
    #3º check if letra_propuesta is in adivinar_word
    elif letra_propuesta in adivinar_word:
        adivinar_word_guion = ''
        opciones_si.append(letra_propuesta)
        for letra in adivinar_word:
            if letra in opciones_si:
                adivinar_word_guion += letra
            else:
                adivinar_word_guion += '-'
    #3º if letra_propuesta has not been said and is not in adivinar_word
    else:
        print('No such letter in the word!')
# the end of the game        
print("""\nThanks for playing!
We'll see how well you did in the next stage""")
