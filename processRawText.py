from __future__ import division
import nltk, re, pprint
import os
from urllib import urlopen

## Obtaining texts
### 1. From web
url = "http://www.gutenberg.org/files/2554/2554.txt"
raw = urlopen(url).read()

### 2. From local files
os.listdir('.')

#### opening the file
f = open('myfile.txt')

#### reading the file in one go
raw = f.read()

#### reading the file line by line
for line in f:
    print line
f.close()

## Tokenization and basic preprocessing
token = nltk.word_tokenize(raw)
type(token)

## Coverting tokens into nltk texts
text = nltk.Text(token)
text.collocations()

### Regular expressions
raw.find('that')
raw.rfind('that')

##### Creating vocabulary item
wordlist = [w for w in nltk.corpus.words.words('en') if w.islower()]

[word for word in wordlist if re.search(r'ed$', word)]
[word for word in wordlist if(re.search(r'^...x..ed$', word))]
[word for word in wordlist if re.search(r'^[ghi][mno][jkl][def]$', word)]

re.search(r'ed', 'walked')

### creating a stemmer using regular expression
re.findall(r'(.*)(ing|ed|es|s)', 'walked')
re.findall(r'(.*?)(ing|es|s)', 'processes') ## non-greedy version
re.findall(r'(.*)(ing|es|s)', 'processes')  ## greedy version
    
def stem(word):
    regexp = r'(.*?)(ing|ly|ed|ious|ies|ive|es|s|ment)?'
    stem, suffix = re.findall(regexp, word)[0]
    return stem

raw = """DENNIS: Listen, strange women lying in pond distributing swords
        is no basis for a system of government"""
tokens = nltk.word_tokenize(raw)
[stem(word) for word in tokens]

porter = nltk.PorterStemmer()
lancaster = nltk.LancasterStemmer()


[porter.stem(word) for word in token]
[lancaster.stem(word) for word in token]








## capturing user input

s = raw_input("Enter  some text")
print s


## String operation


