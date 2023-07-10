
import nltk
import io
import numpy
import random
import string
import warnings
warnings.filterwarnings('ignore')
f = open('C:\depression.txt','r',errors = 'ignore')
#make sure you save the google doc as a txt file to your hard drive (idk if the location matters) and name the txt file as "depression" 
#you may need to change line 9 depending on where you saved this txt file and what you named it
raw = f.read()
raw = raw.lower()
nltk.download('punkt')
nltk.download('wordnet')
#you may delete lines 12 and 13 after running it for the first time
sent_tokens = nltk.sent_tokenize(raw)
word_tokens = nltk.word_tokenize(raw)
print(word_tokens[:45])
#adjust 45 to a lower or higher number to print more or less text
