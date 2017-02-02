import nltk
import re
import numpy as np

## Finding the required resources
cnames = dir(nltk.corpus)
cnames = dir(nltk.corpus.brown)
[word for word in cnames if re.search(r'[Bb]rown', word)]
[word for word in cnames if re.search(r'[Cc]hat', word)]

## word analysis
nword = nltk.corpus.brown.words(categories='news')
len(nword)
fdis = nltk.FreqDist(nword)
fdis['the']
[word for word in fdis.keys() if len(word) > 15]

## conditional frequency distribution
cat = ['news']

## sentence analysis
nsent = nltk.corpus.brown.sents(categories='news')
[len(sent) for sent in nsent]
senLen = sum(len(sent) for sent in nsent)
senNumb = len(nsent)
avgSenLen = senLen/senNumb

## Conditional frequency
genre = ['news', 'hobbies']
nltk.corpus.brown.words[categories = genre]
cfd = nltk.ConditionalFreqDist(
    (gen, word) for gen in genre
    for word in nltk.corpus.brown.words(categories = gen))

cfd['news']['the']
