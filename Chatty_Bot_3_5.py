print('''Hello! My name is Aid.
I was created in 2020.
Please, remind me your name.''')

your_name = input()
# reading a name
print('What a great name you have, {}!'.format(your_name))

print('''Let me guess your age.
Enter remainders of dividing your age by 3, 5 and 7.''')
r3 = int(input()) % 3
r5 = int(input()) % 5
r7 = int(input()) % 7

# reading all remainders
your_age = (((r3)*70)+((r5)*21)+((r7)*15))% 105

print("Your age is {}; that's a good time to start programming!".format(your_age))
