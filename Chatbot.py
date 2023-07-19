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

import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity



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
filtered_list = []

#don't think we need this rn
#stemmer = PorterStemmer()
#stemmed_words = [stemmer.stem(word) for word in word_tokens]
#reduces the words down to their root. Helps the chatbot get familiar with words that come from the same word
#example, reduced, reducing, and reduction have the root word reduce. Uncomment line 38 to print.
#print(stemmed_words)


#Uncomment and adjust 45 to a lower or higher number to print more or less text. only for testing purposes
#print(word_tokens[:45])

#probably dont need this rn either
#stop words are words that can be removed without changing the meaning of the sentence
#for some reason nltk does not recognize "not" as a stopword although it can quite literally change the meaning of any sentence
#so i altered the if condition so "not" is included
#for i in word_tokens:
#	if i.casefold() not in stop_words or i.casefold() == "not":
#		filtered_list.append(i)

#Uncomment this line to print the entire text file without stopwords. only used to show that the code works
#print(filtered_list)

lemmer = nltk.stem.WordNetLemmatizer()
def LemTokens(tokens):
	return[lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct),None) for punct in string.punctuation)
def LemNormalize(text):
	return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

greeting_inputs = ['hi','hello','hey']
greeting_output = ['Hi! Ask me anything about depression','Hello! I am here to answer your depression questions!','Hey, I am happy to answer your doubts about depression']

def greeting(sentence):
	for word in sentence.split():
		if word.lower() in greeting_inputs:
			return random.choice(greeting_output)

def response(user_response):
	chatbot_response = ""
	sent_tokens.append(user_response)
	TfidfVec = TfidfVectorizer(tokenizer = None, stop_words = 'english')
	tfidf = TfidfVec.fit_transform(sent_tokens)
	vals = cosine_similarity(tfidf[-1], tfidf)
	idx = vals.argsort()[0][-2]
	flat = vals.flatten()
	flat.sort()
	req_tfidf = flat[-2]
	if (req_tfidf==0):
		chatbot_response=chatbot_response+"I am sorry, I don't understand you."
		return chatbot_response
	else:
		chatbot_response = chatbot_response+sent_tokens[idx]
		return chatbot_response        

flag = True
print("Hi I am your depression chatbot. I will answer stuff about depression. If you want to exit, type bye.")
while (flag == True):
	user_response = input()
	user_response = user_response.lower()
	if (user_response != 'bye'):
		if (user_response == 'thanks' or user_response == 'thank you'):
			flag = False
			print("Chatbot: you're welcome")
		else:
			if(greeting(user_response) != None):
				print("Chatbot:" + greeting(user_response))
			else:
				print("Chatbot:",end="")
				print(response(user_response))
				sent_tokens.remove(user_response)
	else:
		flag = False
		print("Chatbot: Bye! Take care!")
    
	
x= greeting("hi")
#print(x)
