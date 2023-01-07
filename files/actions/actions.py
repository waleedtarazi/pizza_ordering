from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import AllSlotsReset, EventType
from rasa_sdk.types import DomainDict
import re




def delete_repeated(text):
    pattern = r'(.)\1+'
    return re.sub(pattern,r'\1', text)

PIZZA_SIZES = ['small','meduiem','big','large','xl','s','m','l']
NORM_SIZES = [delete_repeated(x) for x in PIZZA_SIZES]
PIZZA_SIZES_RE = ['no','nop','nah','noo']
PIZZA_TYPES = ['papparoni','mozarella','normal','italian']
NORMLIZED_TYPES = [delete_repeated(x) for x in PIZZA_TYPES]

class ActionResetSlot(Action):

     def name(self) -> Text:
            return "action_reset_slots"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         return [AllSlotsReset()]


class ValidateSimplePizzaForm(FormValidationAction):

    def name(self) -> Text:
        return "validate_simple_pizza_form"

    def validate_pizza_size(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `pizza_size` value."""
        print("in size class", slot_value)    
        if delete_repeated(slot_value.lower()) not in NORM_SIZES :
            dispatcher.utter_message(text=" we can't do such size of pizza!")
            return {"pizza_size": None}
        dispatcher.utter_message(text=f'OK! a {slot_value} pizza.')
        return {"pizza_size": delete_repeated(slot_value)}


    
    def validate_pizza_type(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `pizza_type` value."""
        print("in type class, delete reapated", delete_repeated(slot_value).lower)
        print("types norm",NORMLIZED_TYPES)
        if delete_repeated(slot_value.lower()) not in NORMLIZED_TYPES:
            dispatcher.utter_message(text=f"We no longer serve that pizza.\n We serve {'| '.join(PIZZA_TYPES)}.")
            return {"pizza_type": None}
        dispatcher.utter_message(text=f'allright! {slot_value} pizza will be prepared in just a few moments.')
        return {"pizza_type": delete_repeated(slot_value)}