import nltk
import io
import numpy
import random
import string
import warnings
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
warnings.filterwarnings('ignore')
filtered_list = []

#make sure you save the google doc as a txt file to your hard drive (idk if the location matters) and name the txt file as "depression" 
#you may need to change line 9 depending on where you saved this txt file and what you named it
f = open('C:\depression.txt','r',errors = 'ignore')

raw = f.read()
raw = raw.lower()

#comment out the following lines after running the code once
#nltk.download('punkt')
#nltk.download('wordnet')
#nltk.download("stopwords")

sent_tokens = nltk.sent_tokenize(raw)
word_tokens = nltk.word_tokenize(raw)
stop_words = set(stopwords.words("english"))

#uncomment and adjust 45 to a lower or higher number to print more or less text. only for testing purposes
#print(word_tokens[:45])

#stop words are words that can be removed without changing the meaning of the sentence
#for some reason nltk does not recognize "not" as a stopword although it can quite literally change the meaning of any sentence
#so i altered the if condition so "not" is included
for i in word_tokens:
	if i.casefold() not in stop_words or i.casefold() == "not":
		filtered_list.append(i)

#printing the is only used to show that the code works
#this prints out all the text, aside from the stop words
print(filtered_list)


