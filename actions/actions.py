# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from excel_writer import DataStore


class ActionSaveData(Action):

    def name(self) -> Text:
        return "action_save_data"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        DataStore(
            tracker.get_slot("student_name"),
            tracker.get_slot("student_id"),
            tracker.get_slot("book_id"),
        )
        dispatcher.utter_message(text="Successfully Returned the Book")
        return []


class ActionReturnBook(FormAction):
    def student_name(self) -> Text:
        return "Form_Info"
# Form_Info is the form name and is used in domain.yml as well

    @staticmethod
    def required_slots(tracker: "Tracker") -> List[Text]:
        return ["student_name", "student_id", "book_id"]
# Order in which question is asked

    def slot_mapping(self) -> Dict[Text, Union[Dict, List[Dict[Text, Any]]]]:
        return{
            "student_name": [self, from_text()],
            "student_id": [self, from_text()],
            "book_id": [self, from_text()]
        }

    def submit(
        self,
        dispatcher: "CollectingDispatcher",
        tracker: "Tracker",
        domain: Dict[Text, Any],
    ) -> List[EventType]:
        dispatcher.utter_message("Here is the information that you provided. Confirm?\nStudent Name: {0}\nStudent ID: {1}\nBook ID: {2}".format(
            tracker.get_slot("student_name"),
            tracker.get_slot("student_id"),
            tracker.get_slot("book_id"),
        ))
        return []
