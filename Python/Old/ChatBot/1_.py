
import nltk
# nltk.download('punkt')
from nltk.stem.lancaster import LancasterStemmer
stemmer=LancasterStemmer

import tflearn
import numpy
import json
import random
import tensorflow


with open('intents.json') as file:
    data=json.load(file)
# print(data)


words=[]
docs_x=[]
docs_y=[]
labels=[]

for intents in data['intents']:
    for pattern in intents['patterns']:
        wrds=nltk.word_tokenize(pattern)
        words.extend(wrds)
        docs_x.append(pattern)
        docs_y.append(intents['tag'])

    if intents['tag'] not in labels:
        labels.append(intents['tag'])




#
# words = [stemmer.stem(w.lower()) for w in words]
# words = sorted(list(set(words)))
new_words=[]
for i in words:
    new_words.append(stemmer.stem(i.lower()))
print(new_words)

labels=sorted(labels)
print(words)
print(docs_x)
print(docs_y)
print(labels)