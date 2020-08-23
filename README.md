# Conversational-Bot-ChatBot-for-Restaurant-Search
'Foodie' is a Conversational Bot (ChatBot), which can help users discover restaurants across several Indian cities.

# Problem Statement
'Foodie' is a Conversational Bot (ChatBot), which can help users discover restaurants across several Indian cities. 
The main purpose of the bot is to help users discover restaurants quickly and efficiently and to provide a good restaurant discovery experience. The project brief provided to you is as follows.

The bot takes the following inputs from the user:
- **City:** Take the input from the customer as a text field.\
  For example:\
  Bot: In which city are you looking for restaurants?\
  User: anywhere in Delhi
  #### Important Notes: 
  - Assume that Foodie works only in Tier-1 and Tier-2 cities. I have used the current HRA classification of the cities from [here](https://en.wikipedia.org/wiki/Classification_of_Indian_cities). Under the section 'current classification' on this page, the table categorizes cities as X, Y and Z. Consider 'X ' cities as tier-1 and 'Y' as tier-2. 
  - The bot should be able to identify common synonyms of city names, such as Bangalore/Bengaluru, Mumbai/Bombay etc.
 
  Chatbot will provide results for tier-1 and tier-2 cities only, while for tier-3 cities, it should reply back with something like "We do not operate in that area yet".
- **Cuisine Preference:** Take the cuisine preference from the customer. The bot will list out the following six cuisine categories (*Chinese, Mexican, Italian, American, South Indian & North Indian*) and the customer can select any one out of that.\
  Following is an example for the same:\
  Bot: What kind of cuisine would you prefer?
  - Chinese
  - Mexican
  - Italian
  - American
  - South Indian
  - North Indian 
  
  User: I’ll prefer Italian!
  
- **Average budget for two people:** Segment the price range (average budget for two people) into three price categories: lesser than 300, 300 to 700 and more than 700. The bot should ask the user to select one of the three price categories.\
  For example:\
  Bot: What price range are you looking at?
  - Lesser than Rs. 300
  - Rs. 300 to 700
  - More than 700
 
  User: in range of 300 to 700
  
  *While showing the results to the user, the bot displays the top 5 restaurants in a sorted order (descending) of the average Zomato user rating (on a scale of 1-5, 5 being the highest). The format will be: {restaurant_name} in {restaurant_address} has been rated {rating}.*
  
- **Email Preference:** Finally, the bot will ask the user whether he/she wants the details of the top 10 restaurants on email. If the user replies 'yes', the bot will ask for user’s email id and then send it over email. Else, just reply with a *'goodbye'* message. 
  The mail should have the following details for each restaurant:  
  - Restaurant Name
  - Restaurant locality address
  - Average budget for two people
  - Zomato user rating

# Technical Informations
- RASA Framework is used here for the Natural Language Processing, Intent & Entity Extraction.
- For Restaurant search, Zomato API is used. 
  - For using Zomato API, please generate an API key from [here](https://developers.zomato.com/api?lang=tr) if you dont have it. (max 1000 API calls/day).
  - Next Inside the actions.py file, there is a method named get_restaurants(). Replace the <your_user_key> by your Zomato API key(It will look like a GUID of raw16/raw32 type). - For NLP processing, 'supervised_embeddings' is used which can be changed to 'pretrained_embeddings_spacy'. Benefit of using 'supervised_embeddings' is that the learning happens from the application only without considering any prior knowledge of any word in any language. 'pretrained_embeddings_spacy' is used in case the training data is very less and the scenario is very generic. Example - We should avoid using pretrained embeddings for Bank Domain as some words like Balance etc would mean different in Bank Domain and Generic Scenario. Supervised Learning will start word embedding from the application training data only without considering any prior knowledge. Please refer [here](https://rasa.com/docs/rasa/nlu/choosing-a-pipeline/#id16) for further help on choosing the embedding type.
- For all the actions, we have used Python as a programming language and so Python 3.6+ should be installed 
- For sending e-Mail from Chatbot, we need to have a Email ID to be created for ChatBot, which will be used as sender to send emails to customers. Please add your new email id for Chatbot in actions.py file. Goto method init() of class EmailService and replace <chatbot_email> by the email id and <chatbot_email_pwd> by password. 

# Using the Chatbot
1. Download the project
2. Requirements: 
   1. Python 3.6+
   2. Visual Studio: (For Windows only)
      - Open the Microsoft Visual Studio link: https://visualstudio.microsoft.com/downloads/
      - Select ‘Community version 2019’
      - Download the installer and select VC++ Build tools on the list
   3. Creating a virtual environment : We strongly recommend that you create a virtual environment before installing Rasa and Rasa X.
      Virtual environment tools like virtualenv and virtualenvwrapper provide isolated Python environments. They help you install packages without any dependency conflicts and root privileges.
      - For Windows:
        You can create a virtual environment by opening the command prompt and typing the following code:\
        C:\> python3 -m venv --system-site-packages ./venv\
        You can activate the virtual environment by typing the following code:\
        C:\> .\venv\Scripts\activate\
      - For MacOS:
        You can create a virtual environment by opening the command prompt and typing the following code:\
        $ python3 -m venv --system-site-packages ./venv\
        You can activate the virtual environment by typing the following code:\
        $ source ./venv/bin/activate\
   4. Installing Rasa and Rasa X: 
      You can install both Rasa and Rasa X using the following code:
      pip install rasa-x --extra-index-url https://pypi.rasa.com/simple
      Use the following code only if you want to install Rasa:
      pip install rasa 
   5. Install Rasa NLU and Spacy in the same command prompt:
      pip install rasa[spacy]
      python -m spacy download en_core_web_md
      python -m spacy link en_core_web_md en
      
  **Note: If the system prompts you to upgrade pip, then use the following commands:
  *For Windows:*
  python -m pip install --upgrade pip
  *For MacOS:*
  pip install pip –upgrade
  pip install setuptools –upgrade**
  
  ***List of All Commands in RASA check [here](https://rasa.com/docs/rasa/user-guide/command-line-interface/)***

#### Training
- For Training, execute the command rasa train nlu
#### Interactive Learning
- Rasa provides option to train the chatbot model using the Interactive Approach.
- Please refer [here](https://rasa.com/docs/rasa/core/interactive-learning/) for Interactive Learning
- In Command Prompt enable the virtual environment and go inside the folder where the project is stored
  - Run command rasa run actions
  - Open one more terminal, enable virtual environment and go inside the folder where the project is stored, and run command rasa interactive(make sure the action server is running)
#### Testing the ChatBot
- In Command Prompt enable the virtual environment and go inside the folder where the project is stored
  - Run command rasa run actions
  - Open one more terminal, enable virtual environment and go inside the folder where the project is stored, and run command rasa shell(make sure the action server is running)
  
  
  
