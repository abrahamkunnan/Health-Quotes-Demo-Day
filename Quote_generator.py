import nltk
from nltk.tokenize import word_tokenize
import sklearn
from nltk.stem import WordNetLemmatizer
import random
user=input('1.Ask Questions about depressoin\n2.Tell us how you feel,and we\'ll inspire you with a quote')
quotes={
    "sad":[
        "The pain you feel today is the strength you feel tomorrow. "
        ,"Tears come from the heart and not from the brain.",
        "“Cheer up, my dear. After every storm comes the sun. Happiness is waiting for you ahead.”",
        "“What doesn\'t kill you makes you stronger.”",
        "“Life is a mixture of sunshine and rain, teardrops and laughter, pleasure and pain. Just remember, there was never a cloud that the sun couldn\'t shine through.”",
        "“Good people are good because they\'ve come to wisdom through failure.”",
        "“Life is too short for us to dwell on sadness. Cheer up and live life to the fullest.”",
        "Sometimes you have to fight through your worst days in order to earn the best days of your life.",
        "If you\'re going through a hard time right now, make sure you do something today that makes you smile.",
        "Sadness is but a wall between two gardens.",
        "Life\'s under no obligation to give us what we expect.",
        ""

        
        ],
    "depressed":[
        "It\'s OK to not feel OK",
        "You\'re not alone",
        "You can move forward in the face of your depression",
        "Your story isn\'t over",
        "“If you are still breathing maybe it is not such a bad day after all.”",
        "“You alone are enough. You have nothing to prove to anybody.”",
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
        ""


       
        



  ],
  "death":[
      "Our dead are never dead to us until we have forgotten them",
      "The bitterest tears shed over graves are for words left unsaid and deeds left undone.",
      "You know, a heart can be broken, but it keeps on beating, just the same",
      ""
  ],
    "frustrated":[
        "“If you really love something set it free. If it comes back it\'s yours, if not it wasn\'t meant to be.”",
        "“People will always throw stones in your path. What will happen depends on what you make out of it a wall or a bridge! So cheer up and move on.”",
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
        ""


    ]
    }
def quote():
    user_feeling=input('How do you feel?')
    feeling_tokenized=nltk.work_tokenize(user_feeling)

