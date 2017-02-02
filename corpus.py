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

model = ['can', 'could', 'would', 'will']

for item in model:
    print 'news', item, ":", cfd['news'][item]
    print 'hobbies', item, ":", cfd['hobbies'][item]

## finding the fraction of stopword in a given text

stopword = nltk.corpus.stopwords.words('english')
newsword = nltk.corpus.brown.words(categories='news')

nonstopword = [w for w in newsword if w.lower() not in stopword]
len(nonstopword)/len(newsword)

## Finding the name
nltk.corpus.names.fileids()

cfd = nltk.ConditionalFreqDist((fileid, names[-1]) for fileid in nltk.corpus.names.fileids()
          for names in nltk.corpus.names.words(fileid))

cfd.items()[:10]
cfd.plot()

## wordnet
from nltk.corpus import wordnet as wn
wn.synsets('motorcar')






