"""
Script helping you generate random strings
"""
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from argparse import ArgumentParser
from secrets import choice
from time import time

start = time()


parser = ArgumentParser(description='Generate (pseudo)random string')

parser.add_argument("-l", "--lowercase", action="store_true", default=False, help="use lowercase ascii letters")
parser.add_argument("-u", "--uppercase", action="store_true", default=False, help="use uppercase ascii letters")
parser.add_argument("-d", "--digits", action="store_true", default=False, help="use digits")
parser.add_argument("-p", "--punctuation", action="store_true", default=False, help="use punctuation")
parser.add_argument("-c", "--copy", action="store_true", default=False, help="copy generated string to clipboard (requires pyperclip)")
parser.add_argument("length", action="store", type=int, help="length of generated string")

args = parser.parse_args()

print('Length choosen: ' + str(args.length))
cont = []
out = ''

if args.lowercase:
    lowercase = list(ascii_lowercase)
    cont.extend(lowercase)
    print('Adding ascii lowercase letters...')
if args.uppercase:
    uppercase = list(ascii_uppercase)
    cont.extend(uppercase)
    print('Adding ascii uppercase letters...')
if args.digits:
    digits = list(digits)
    cont.extend(digits)
    print('Adding digits...')
if args.punctuation:
    punctuation = list(punctuation)
    cont.extend(punctuation)
    print('Adding punctuation...\n')


for n in range(args.length):
    out += choice(cont)
print(out)

if args.copy:
    try:
        from pyperclip import copy
        copy(out)
        print('Copied to clipboard!')
    except ImportError:
        print('No pyperclip module - not copied.')

print('Execution time: %s seconds' % (time() - start))
