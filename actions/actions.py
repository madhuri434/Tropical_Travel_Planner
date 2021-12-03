#from typing import Any, Text, Dict, List

#from rasa_sdk import Action, Tracker
#from rasa_sdk.executor import CollectingDispatcher
#from weather import Weather


 #class ActionHelloWorld(Action):

    #def name(self) -> Text:
     #   return "action_weather_api"

    #def run(self, dispatcher: CollectingDispatcher,
    #tracker: Tracker,
      #domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #city = tracker.latest_message['text']

        #temp = int(Weather(city)['temp']-273)

       # dispatcher.utter_template("utter_temp", tracker, temp = temp)

       # return []