# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet

# http://weather.yahoo.com
# from weather import Weather, Unit

import logging
import requests
import json


logger = logging.getLogger(__name__)

class ActionJoke(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_joke"

    def run(self, dispatcher, tracker, domain):
        # what your action should do
        request = requests.get('http://api.icndb.com/jokes/random').json() #make an apie call
        joke = request['value']['joke'] #extract a joke from returned json response
        dispatcher.utter_message(joke) #send the message back to the user
        return []

class ActionGetWeather(Action):
    def name(self):
        return 'action_weather_ActionGetWeather'

    def run(self, dispatcher, tracker, domain):
        weather = Weather(unit=Unit.CELSIUS)
        gpe = ('Singapore', tracker.get_slot('GPE'))[bool(tracker.get_slot('GPE'))]
        result = weather.lookup_by_location(gpe)
        if result:
            condition = result.condition
            city = result.location.city
            country = result.location.country
            dispatcher.utter_message('It\'s ' + condition.text + ' and ' + condition.temp + '°C in ' +
                                     city + ', ' + country + '.')
        else:
            dispatcher.utter_message('We did not find any weather information for ' + gpe + '. Search by a city name.')
        return

class ActionWeather(Action):

    def name(self):
        return 'actions_ActionWeather'
    
    def run(self,dispatcher, tracker, domain):

        from apixu.client import ApixuClient
        api_key = "f5d0a214ccf44880ace61427180103"
        client = ApixuClient(api_key)

        loc = tracker.get_slot('location')
        current = client.getCurrentWeather(q=loc)

        country = current['location']['country']
        city = current['location']['name']
        condition = current['current']['condition']['text']
        temperature_c = current['current']['temp_c']
        humidity = current['current']['humidity']
        wind_mph = current['current']['wind_mph']

        response = """It is currently {} in {} at the moment. The temperature is {}  degree the humidity is {}% and the wind speed  is {} mph.""".format(condition,city,temperature_c,humidity,wind_mph)

        dispatcher.utter_message(response)
        return [SlotSet('location',loc)]
		
class Actiondadjoke(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_dadjoke"

    def run(self, dispatcher, tracker, domain):
        # what your action should do
        
        request = json.loads(requests.get('http://jokes.guyliangilsing.me/retrieveJokes.php?type=dadjoke').text)  # make an api call
        dadjoke = request['joke']  # extract a joke from returned json response
        dispatcher.utter_message(dadjoke)  # send the message back to the user
        return []

class Actionpun(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_pun"

    def run(self, dispatcher, tracker, domain):
        # what your action should do
        request = json.loads(requests.get('https://some-random-api.ml/meme').text)  # make an api call
        pun = request['text']  # extract a joke from returned json response
        dispatcher.utter_message(pun)  # send the message back to the user
        return []
    
class Actionpandafact(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_pandafact"

    def run(self, dispatcher, tracker, domain):
        # what your action should do
        request = json.loads(requests.get('https://some-random-api.ml/pandafact').text)  # make an api call
        pun = request['fact']  # extract a joke from returned json response
        dispatcher.utter_message(pun)  # send the message back to the user
        return []

class ActionCatFact(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_catFact"

    def run(self, dispatcher, tracker, domain):
        # what your action should do
        request = json.loads(requests.get('https://catfact.ninja/fact').text)  # make an api call
        catFact = request['fact']  # extract a catFact from returned json response
        dispatcher.utter_message(catFact)  # send the message back to the user
        return []

class ActionDogFact(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_dogFact"

    def run(self, dispatcher, tracker, domain):
        # what your action should do
        request = json.loads(requests.get('https://some-random-api.ml/dogfact').text)  # make an api call
        dogFact = request['fact']  # extract a dogFact from returned json response
        dispatcher.utter_message(dogFact)  # send the message back to the user
        return []
