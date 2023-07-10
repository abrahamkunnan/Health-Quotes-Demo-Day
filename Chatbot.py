
import nltk
import io
import numpy
import random
import string
import warnings
warnings.filterwarnings('ignore')
f = open('C:\depression.txt','r',errors = 'ignore')
raw = f.read()
raw = raw.lower()
sent_tokens = nltk.sent_tokenize(raw)
word_tokens = nltk.word_tokenize(raw)
print(word_tokens[:45])
