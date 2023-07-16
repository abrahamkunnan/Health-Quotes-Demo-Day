import nltk
import io
import numpy
import random
import string
import warnings
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import sys
print(sys.version)

f = open('C:\depression.txt','r',errors = 'ignore')
raw = f.read()
raw = raw.lower()

filtered_list = []

#comment out the following lines after running the code once
#nltk.download('punkt')
#nltk.download('wordnet')
#nltk.download("stopwords")

sent_tokens = nltk.sent_tokenize(raw)
word_tokens = nltk.word_tokenize(raw)
stop_words = set(stopwords.words("english"))

stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in word_tokens]
#reduces the words down to their root. Helps the chatbot get familiar with words that come from the same word
#example, reduced, reducing, and reduction have the root word reduce. Uncomment line 38 to print.
#print(stemmed_words)


#Uncomment and adjust 45 to a lower or higher number to print more or less text. only for testing purposes
#print(word_tokens[:45])

#stop words are words that can be removed without changing the meaning of the sentence
#for some reason nltk does not recognize "not" as a stopword although it can quite literally change the meaning of any sentence
#so i altered the if condition so "not" is included
for i in word_tokens:
	if i.casefold() not in stop_words or i.casefold() == "not":
		filtered_list.append(i)

#Uncomment this line to print the entire text file without stopwords. only used to show that the code works
#print(filtered_list)

greeting_inputs = ['hi','hello','hey']
greeting_output = ['Hi! Ask me anything about depression','Hello! I am here to answer your depression questions!','Hey, I am happy to answer your doubts about depression']

def greeting(sentence):
	for word in sentence.split():
		if word.lower() in greeting_inputs:
			return random.choice(greeting_output)

x= greeting("hi")
#uncomment this line to execute greeting
#print(x)
