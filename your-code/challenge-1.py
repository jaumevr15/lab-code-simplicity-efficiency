"""
This is a dumb calculator that can add and subtract whole numbers from zero to five.
When you run the code, you are prompted to enter two numbers (in the form of English
word instead of number) and the operator sign (also in the form of English word).
The code will perform the calculation and give the result if your input is what it
expects.

This code is awesome because Jaume cleaned it, you are welcome!
"""
#Questions to be asked to get the desired input
def questions():
    print('Welcome to this calculator!''\n''It can add and subtract whole numbers from zero to five')
    a = input('Please choose your first number (zero to five): ')
    b = input('What do you want to do? plus or minus: ')
    c = input('Please choose your second number (zero to five): ')
    return a, b, c
a,b,c = questions()

#Creating translating dictionaries and accepted values.
eng_to_num = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,'ten': 10}
num_to_eng = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten'}
operators = {'plus': 11, 'minus': 12}
correct = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}

#Checking input is correct
while a not in correct and b not in operators and c not in correct:
    print("I am not able to answer this question. Check your input.")
    questions()

#Two functions to check the equivalent number english - integer
def to_dict(x):
    return num_to_eng[x]
def to_int(x):
    return eng_to_num[x]

#The program
if b == 'plus':
    d = to_int(a) + to_int(c)
    print(f"{a} plus {c} equals {to_dict(d)}")
elif b == 'minus':
    d = abs(to_int(a) - to_int(c))
    if to_int(a) - to_int(c) < 0:
        print(f'{a} minus {c} equals negative {to_dict(d)}')
    else:
        print(f"{a} minus {c} equals {to_dict(d)}")

print("Thanks for using this calculator, goodbye :)")
