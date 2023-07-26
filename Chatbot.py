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
ps = PorterStemmer()
#filtered_list = []

quotes={
	"none": [""],
    "sadness":[
        "The pain you feel today is the strength you feel tomorrow.",
		"Tears come from the heart and not from the brain.",
        "Cheer up, my dear. After every storm comes the sun. Happiness is waiting for you ahead.",
        "What doesn\'t kill you makes you stronger.",
        "Life is a mixture of sunshine and rain, teardrops and laughter, pleasure and pain. Just remember, there was never a cloud that the sun couldn\'t shine through.",
        "Good people are good because they\'ve come to wisdom through failure.",
        "Life is too short for us to dwell on sadness. Cheer up and live life to the fullest.",
        "Sometimes you have to fight through your worst days in order to earn the best days of your life.",
        "If you\'re going through a hard time right now, make sure you do something today that makes you smile.",
        "Sadness is but a wall between two gardens.",
        "Life\'s under no obligation to give us what we expect.",
        "We cannot solve problems with the kind of thinking we employed when we came up with them."
        "What brings us to tears, will lead us to grace. Our pain is never wasted.",
        "Every life has a measure of sorrow, and sometimes this is what awakens us.",
        "People cry, not because they are weak. It is because they've been strong for too long. ",
        "Your greatest highs come from overcoming your greatest lows. ",
        "First, accept sadness. Realize that without losing, winning isn\'t so great. ",
        "When everything seems to be going against you, remember that the airplane takes off against the wind, not with it.",
        "You cannot always control what goes on outside. But you can always control what goes on inside.",
        "Nothing ever goes away until it teaches us what we need to know. ",
        "If there is no struggle, there is no progress.",
        "Courage is like a muscle. We strengthen it by use.",
        "If you don\'t like the road you\'re walking, start paving another one.",
        "Life has got all those twists and turns. You've got to hold on tight and off you go.", 
        ],

    "depressed":[
        "It\'s OK to not feel OK",
        "You\'re not alone",
        "You can move forward in the face of your depression",
        "Your story isn\'t over",
        "If you are still breathing maybe it is not such a bad day after all.",
        "You alone are enough. You have nothing to prove to anybody.",
        "It is never too late to be what you might have been.",
        "Don\'t close the book when bad things happen in your life! Just turn the page and start a new chapter!",
        "Please remember that you\'re capable, brave and loved even when it feels like you\'re not."
        "Do not give the past the power to define your future.",
        "Even the darkest hour only has 60 minutes.",
        "Don\'t hate yourself for everything you aren\'t. Instead, love yourself for everything you are."
        "Running away from your problems is a race you\'ll never win. Instead, reach out for help and try to confront them.",
        "Don\'t let your struggle become your identity. After all, you are so much more than just your illness."
        "Be proud of who you are, instead of ashamed of how someone else sees you.",
        "Crying doesn\'t mean that you\'re weak. Since birth, it\'s always been a sign that you\'re alive.",
        "Don\'t dwell on those who hold you down. Instead, cherish those who helped you up.",
        "Even if you can\'t see any reason to keep on going, then it doesn\'t mean that there aren\'t any. It just means that in that moment, your depression is telling you even more lies than usual.",
        "Even the worst depressive episodes won\'t last forever.",
        "If you need a confidence booster, then remind yourself of all the difficult things you\'ve endured and overcome."
        "When your depression says, 'Give up', hope whispers, 'Try one more time'.",
        "One day, if not already, your refusal to give up will inspire someone else.",
        "Please remember that having a bad day does not mean you have or will have a bad life.",
        "Hope is one of the most powerful emotions a person can have. Combine it with determination and there\'s no stopping you.",
        "Never put the key to your happiness in someone else\'s pocket.",
        "Just because you have a mental illness, it doesn't mean that you are that illness. You're still a person just like everybody else.",
        "Sometimes, you just need to cry your eyes out to be able to keep going. And you know what? That's OK.",
        "Healing is a process, not an event. Give it time. Good things happen to those who never give up.",
        "When something goes wrong, take a moment to be thankful for all the things in your life that are going right.",
        "Never forget that you are worthy of love and respect.",
        "Don\'t let yesterday take up too much of today.",
        "Experience is a hard teacher because she gives the test first, the lesson afterwards.",
        "When everything seems to be going against you, remember that the airplane takes off against the wind, not with it.",
        "Life has got all those twists and turns. You've got to hold on tight and off you go.",
  ],
  
    "frustrated":[
        "If you really love something set it free. If it comes back it\'s yours, if not it wasn\'t meant to be.",
        "People will always throw stones in your path. What will happen depends on what you make out of it a wall or a bridge! So cheer up and move on.",
        "Never give up. Today is hard, tomorrow will be worse, but the day after tomorrow will be sunshine.",
        "Life is like riding a bicycle. To keep your balance, you must keep moving.",
        "Fall seven times, stand up eight.",
        "Tough times never last, but tough people do.",
        "Some people go through hard times, so bad that they can\'t even talk about it, but no matter what, we should never give up.",
        "Let them ridicule you, laugh at you, hurt you & ignore you but never let them stop you.",
        "It does not matter how slowly you go as long as you do not stop.",
        "I never lose. I either win or learn.",
        "Our greatest glory is not in never falling but in rising every time we fall.",
        "You\'re allowed to scream, you\'re allowed to cry, but do not give up.",
        "It always seems impossible until it\'s done.",
        "You never fall until you stop trying."
        "Don't go around saying the world owes you a living. The world owes you nothing. It was here first.",
        "Stay away from those people who try to disparage your ambitions. Small minds will always do that, but great minds will give you a feeling that you can become great too.",
        "It is better to fail in originality than to succeed in imitation.",
        "You learn more from failure than from success. Don\'t let it stop you. Failure builds character.",
        "Setting goals is the first step in turning the invisible into the visible. ",
        "The elevator to success is out of order. You\'ll have to use the stairs, one step at a time.",
        "When everything seems to be going against you, remember that the airplane takes off against the wind, not with it.",
        "Nothing is impossible. The word itself says Im possible!",
        ""
    ]
    }

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
greeting_output = ['Hi! Ask me anything about depression\n','Hello! I am here to answer your depression questions!\n','Hey, I am happy to answer your doubts about depression\n']

def greeting(sentence):
	for word in sentence.split():
		if word.lower() in greeting_inputs:
			return random.choice(greeting_output)

def get_quote(emotion):
    return random.choice(quotes.get(emotion,[]))


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
print("Hi I am your depression chatbot. I will answer stuff about depression and also give you inspirational quotes if you tell me how you feel. If you want to exit, type bye.\n")
while (flag == True):
	user_response = input()
	user_response = user_response.lower()
	if (user_response != 'bye'):
		if (user_response == 'thanks' or user_response == 'thank you' or user_response == 'thx'):
			print("\nChatbot: you're welcome\n")
		else:
			if(greeting(user_response) != None):
				print("\nChatbot:" + greeting(user_response))
			else:
				print("\nChatbot:",end="")
				print(response(user_response))
				feeling_tokenized=nltk.word_tokenize(user_response.lower())
				stemmed=[]
				for word in feeling_tokenized:
					stemmed.append(ps.stem(word))

				for word in stemmed:
					if word == 'depress':
						emotion ="depressed"
					elif word == 'sad':
						emotion = 'sadness'
					elif word == 'frustrat':
						emotion = 'frustrated'
					else:
						emotion = 'none'
				quote=get_quote(emotion)
				print("Chatbot: "+ "'" + quote + "'"+"\n")
				sent_tokens.remove(user_response)
	else:
		flag = False
		print("Chatbot: Bye! Take care!")
    
	
#x= greeting("hi")
#print(x)
