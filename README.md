Welcome to Health Quotes! Here are the instructions to run our project. 

Keep in mind, this code only works with windows devices, it does not have MacOS compatibility

This code is not specific to any IDE meaning that it can run on almost any Python IDE. Keep in mind we used VSCode and are not responsible for any errors you may get while trying to run on any other IDE

Conduct a pip install for the libraries nltk, random, and scikit-learn. If you can import these without errors, no action needs to be taken regarding imports

If you get errors for importing some of the libraries (in my experience nltk was problematic for me), you must set up a virtual environment in VSCode and do the pip installs in your venv.

If you must set up a venv, ensure that your machine does not block scripts from running. If your machine DOES block scripts from running, change the execution policy to 'unrestricted' as the default is most likely 'restricted'

DO NOT RENAME ANY FILES YOU DOWNLOAD FROM OUR GITHUB REPO

You MUST download our depression.txt and it MUST be saved in your C: drive. For minimum hassle save it as a file within the C: drive and NOT WITHIN A FOLDER IN YOUR C: DRIVE

Download flaskapp.py

Download home.html, questions.html, and quotes.html

In your folder where flaskapp.py is located, create another folder named 'templates'. Place the html files in the templates folder

The application can be started by running flaskapp.py

There are 3 lines of code at the beginning of flaskapp.py that are download statements for nltk features. THESE LINES MUST BE UNCOMMENTED FOR THE FIRST TIME RUNNING FLASKAPP.PY.

After the first run of flaskapp.py, you may comment the 3 download statements as they are unneeded for future use.

After running flaskapp.py, the console should generate one or two links that host the chatbot on your localhost. If the console generates 2 links, both links redirect to the same place.

The links lead to our website! Click around the links and follow the instructions on the website to ensure the best experience with our chatbot
