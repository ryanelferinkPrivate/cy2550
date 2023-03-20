#!/usr/bin/env python2
import sys
import random
import getopt


# constants
words = 4
caps = 0
numbers = 0
symbols = 0
start = ""


# allow access to word bank
dic_file = open("words.txt")
word_bank = dic_file.read().splitlines()
dic_file.close()


try:
    opts, args = getopt.getopt(sys.argv[1:], "h:w:c:n:s:", ["help", "words=", "caps=", "numbers=", "symbols="])
except getopt.GetoptError:
    sys.exit(2)


out = []
symbol_bank = ["~", "!", "@", "#", "$", "%", "^", "&", "*", "\"", ".", ":", ";"]
# initialise i to 0
i = 0


for opt, arg in opts:
    if opt == "-h" or opt == "--help":
        print("usage: xkcdpwgen [-h] [-w WORDS] [-c CAPS] [-n NUMBERS] [-s SYMBOLS]"
              "Generate a secure, memorable password using the XKCD method"
              "optional arguments:"
              "-h, --help                        show this help message and exit"
              "-w WORDS, --words                 WORDS include WORDS words in the password (default=4)"
              "-c CAPS, --caps CAPS              capitalize the first letter of CAPS random words (default=0)"
              "-n NUMBERS, --numbers NUMBERS     insert NUMBERS random numbers in the password (default=0)"
              "-s SYMBOLS, --symbols SYMBOLS     insert SYMBOLS random symbols in the password (default=0)")
        sys.exit()
    elif opt == "-w" or opt == "--words":
        words = int(arg)
    elif opt == "-c" or opt == "--caps":
        caps = int(arg)
    elif opt == "-n" or opt == "--numbers":
        numbers = int(arg)
    elif opt == "-s" or opt == "--symbols":
        symbols = int(arg)

# Output component includes randomised words
rand_words = random.sample(word_bank, words)
out.extend(rand_words)


# adds capitalisation to an i number of words
for i in range(caps):
    out[i] = out[i].capitalize()

# appends numbers to the password
for i in range(numbers):
    r = random.randint(0, 9)
    out.append(r)

# appends symbols to the password
for i in range(symbols):
    r = random.randint(0, len(symbol_bank)-1)
    out.append(symbol_bank[r])

# return
random.shuffle(out)
end = start.join(str(item) for item in out)
print(end)
