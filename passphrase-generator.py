#! /bin/python

import argparse
import secrets



parser = argparse.ArgumentParser(description = 'Generate a Passphrase')

parser.add_argument('-n', '--num', default = 6, type = int, help = 'number of words')
parser.add_argument('-f', '--file', default = 'diceware.wordlist.txt', help = 'dictionary file name')
parser.add_argument('-v', '--verbose', action = 'store_true', help = 'verbose output')

args = parser.parse_args()



with open(args.file) as f:
    words = [word.strip() for word in f]
    password = ' '.join(secrets.choice(words) for i in range(args.num))

    if args.verbose:
        print()
        print(password)
        print()
        print('Number of words:    ' + str(args.num))
        print('Number of letters:  ' + str(len(password)))

    else:
        print(password)

