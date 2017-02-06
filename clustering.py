import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer(min_df=1)
print(vectorizer)
content = ["how to format my hard disk.", "Hard disk format problem"]
X = vectorizer.fit_transform(content)
vectorizer.get_feature_names()
print X.toarray().transpose()

post1 = '''This is a toy post about machine learning.
          Actually, it contains not much interesting stuff'''

post2 = '''Imaging databases can get huge'''

post3 = '''Most imaging databases safe images permamently'''

post4 = '''Imaging databases store images'''

post5 = '''Imaging databases store images. Imaging databases store images.
         Imaging databases store images'''

text = post1.split() + post2.split() + post3.split() + post4.split() + post5.split()
vectorizer.fit_transform(text)

