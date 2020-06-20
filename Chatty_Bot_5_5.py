def greet(bot_name, birth_year):
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.')

def remind_name():
    print('Please, remind me your name.')
    name = input()
    print('What a great name you have, ' + name + '!')

def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    r3 = int(input())
    r5 = int(input())
    r7 = int(input())
    age = (r3 * 70 + r5 * 21 + r7 * 15) % 105
    print("Your age is " + str(age) + "; that's a good time to start programming!")

def count():
    print('Now I will prove to you that I can count to any number you want.')
    number = int(input())
    num = 0
    while num <= number:
        print(num, '!')
        num += 1

def test():
    print("Let's test your programming knowledge.")
    print("""Why do we use methods?
        1. To repeat a statement multiple times.
        2. To decompose a program into several small subroutines.
        3. To determine the execution time of a program.
        4. To interrupt the execution of a program.""")
    respuesta = input()
    while respuesta != '2':
        respuesta = input('Please, try again.')
            
    print('Completed, have a nice day!')

def end():
    print('Congratulations, have a nice day!')

greet('Aid', '2020')
remind_name()
guess_age()
count()
test()
end()
