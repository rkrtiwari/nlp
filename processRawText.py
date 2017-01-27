from __future__ import division
import nltk, re, pprint
from urllib import urlopen

url = "http://www.gutenberg.org/files/2554/2554.txt"
raw = urlopen(url).read()

token = nltk.word_tokenize(raw)
type(token)

text = nltk.Text(token)
text.collocations()

raw.find('that')
raw.rfind('that')


url = 'http://www.bbc.com/sport/tennis/38760568'
raw = urlopen(url).read()


f = open('myfile.txt')
raw = f.read()

import os
os.listdir('.')

for line in f:
    print line


## capturing user input

s = raw_input("Enter  some text")
print s


## String operation


