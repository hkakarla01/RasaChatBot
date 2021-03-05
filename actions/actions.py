# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import UserUtteranceReverted
from rasa_sdk.executor import CollectingDispatcher

from database_connectivity import updatevalue
from store_excel import store_csv


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#        dispatcher.utter_message(template="utter_greet",name="Terminator")
#         with open("userdata.txt","a") as file:
#             s="{0},{1},{2}".format(tracker.get_slot("email"),tracker.get_slot("phone-number"),tracker.get_slot("feedback"))
#             file.write(s+"\n")
        #updatevalue(tracker.get_slot("email"),tracker.get_slot("phone-number"),tracker.get_slot("feedback"))
        store_csv(tracker.get_slot("email"),tracker.get_slot("phone-number"),tracker.get_slot("feedback"))
        dispatcher.utter_message("Thanks for providing the information")
        return []

class fallback(Action):

    def name(self) ->Text:
        return "action_default_fallback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("This is a fall back message")
        return [UserUtteranceReverted()]
