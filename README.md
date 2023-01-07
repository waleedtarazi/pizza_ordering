# Give me my PIZZA

## Features
- respone for uesrs input considering the varity of inputes    
- response even if user says: i hate you, jfdsfks, ...etc

## Tech
my_pizza uses a number of open source to work properly:

- [RASA](https://rasa.com/) - chatbot builder!

## Installation

- [RASA](https://rasa.com/) v 3.4.0
- [python](https://python.org/) v 3.8
## files
- Actions: contain special responses for users input and some Developer’s functions (like retrieve data…etc.)
- Data: 
    - Nlu: the training examples for each Intent and Entity
    - Rules: defined rules for users input and how to response for
    - Stories: scenario for conversations
- Models: trained models
- Test: some test stories and scenarios 
- Results: the confusion matrix for:
    - DIET classifier both Intent and Entity
    - TED policies which is responsible for picking the right next actio
