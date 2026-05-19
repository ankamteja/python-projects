import random
import string

length = int(input("password len: "))
numbers = string.digits
spe_characters = string.punctuation
uc = string.ascii_uppercase
lc = string.ascii_lowercase
characters = numbers+spe_characters+uc+lc

def gen_pass():
    random_pass = ''.join(random.choices(characters, k=length))
    return random_pass;

def cont():
    cont1 = input("Wanna continue(yes or no): ").capitalize()
    return cont1;
while True:
    print(gen_pass())
    Result = cont()
    if Result == 'Yes':
        continue
    else:
        break