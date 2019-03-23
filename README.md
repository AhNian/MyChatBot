# MyChatBot
In order to run need to install RASA Core

Things to install
1)Python 3.6
2)pip install rasa_core
3)pip install rasa_nlu[tensorflow]
5)pip install spacy
5)choco install make

Once downloaded the file
In python command prompt run pip install -r requirements.txt

steps to run
1) make train-nlu
2) make train-core
3) python main.py
4) python -m rasa_core_sdk.endpoint --actions actions (on another python command prompt)
5) in internet browser go to http://localhost:5000/
