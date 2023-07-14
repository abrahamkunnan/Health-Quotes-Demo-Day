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


raw = f.read()
raw = raw.lower()


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
print(x)
#basic function made for greeting purposes, I was supposed to get to the chatbot answering questions about depression
#but that required sklearn library which I informed you guys was giving me problems due to sublime text running on python 2 default
#I promise to get you a version which can answer questions soon
#for now tamper with the x variable and pass in values of hello and hey within the greeting function to see how it works
#the code will soon be able for you to actually type your questions instead of passing them into the function and running the code
