### Required Libraries ###
from datetime import datetime
from dateutil.relativedelta import relativedelta

### Constants
MIN_INVESTMENT_AMT = 5000

### Functionality Helper Functions ###
def parse_int(n):
    """
    Securely converts a non-integer value to integer.
    """
    try:
        return int(n)
    except ValueError:
        return float("nan")

def parse_float(n):
    """
    Securely converts a non-numeric value to float.
    """
    try:
        return float(n)
    except ValueError:
        return float("nan")
        
def build_validation_result(is_valid, violated_slot, message_content):
    """
    Define a result message structured as Lex response.
    """
    if message_content is None:
        return {"isValid": is_valid, "violatedSlot": violated_slot}

    return {
        "isValid": is_valid,
        "violatedSlot": violated_slot,
        "message": {"contentType": "PlainText", "content": message_content},
    }


### Dialog Actions Helper Functions ###
def get_slots(intent_request):
    """
    Fetch all the slots and their values from the current intent.
    """
    return intent_request["currentIntent"]["slots"]


def elicit_slot(session_attributes, intent_name, slots, slot_to_elicit, message):
    """
    Defines an elicit slot type response.
    """
    print(f'DEBUG - elicit_slot - session_attributes: {session_attributes}, slot_to_elicit: {slot_to_elicit}, message: {message}')
    return {
        "sessionAttributes": session_attributes,
        "dialogAction": {
            "type": "ElicitSlot",
            "intentName": intent_name,
            "slots": slots,
            "slotToElicit": slot_to_elicit,
            "message": message,
        },
    }


def delegate(session_attributes, slots):
    """
    Defines a delegate slot type response.
    """

    print(f'DEBUG - DELEGATE - session_attributes: {session_attributes}, slots: {slots}')
    return {
        "sessionAttributes": session_attributes,
        "dialogAction": {
            "type": "Delegate", 
            "slots": slots},
    }


def close(session_attributes, fulfillment_state, message):
    """
    Defines a close slot type response.
    """
    print(f'DEBUG - CLOSE - SUCCESS! - session_attributes: {session_attributes}, fulfillment_state: {fulfillment_state}, message: {message}')
    response = {
        "sessionAttributes": session_attributes,
        "dialogAction": {
            "type": "Close",
            "fulfillmentState": fulfillment_state,
            "message": message,
        },
    }

    return response


### Intents Handlers ###
def recommend_portfolio(intent_request):
    """
    Performs dialog management and fulfillment for recommending a portfolio.
    """

    missing_data = True

    first_name = get_slots(intent_request)["firstName"]
    age = get_slots(intent_request)["age"]
    investment_amount = get_slots(intent_request)["investmentAmount"]
    risk_level = get_slots(intent_request)["riskLevel"]
    source = intent_request["invocationSource"]

    if all(v is not None for v in [first_name, age, investment_amount, risk_level]):
        missing_data = False

    # Log
    print(f'DEBUG - slot values: {source}, {first_name}, {age}, {investment_amount}, {risk_level}, *** {missing_data} ***')
    
    if source == "DialogCodeHook" and missing_data == True:
        # Perform basic validation on the supplied input slots.
        # Use the elicitSlot dialog action to re-prompt
        # for the first violation detected.

        # Gets all the slots
        slots = get_slots(intent_request)
        
        # Validate age and investmentAmount
        validation_result = validate(age, investment_amount)
        
        if not validation_result["isValid"]:
            
            # Clean invalid slot
            slots[validation_result["violatedSlot"]] = None  

            # Returns an elicitSlot dialog to request new data for the invalid slot
            return elicit_slot(
                intent_request["sessionAttributes"],
                intent_request["currentIntent"]["name"],
                slots,
                validation_result["violatedSlot"],
                validation_result["message"])

        # Fetch current session attibutes
        output_session_attributes = intent_request["sessionAttributes"]
        
        return delegate(output_session_attributes, get_slots(intent_request))
    
    # Get investment recommendation
    recommendation = getRecommendationForRiskLevel(risk_level)

    # Return a message with the initial recommendation based on the risk level.
    return close(
        intent_request["sessionAttributes"],
        "Fulfilled",
        {
            "contentType": "PlainText",
            "content": 
                """{}, thank you for your information. Based on the risk level you defined, my recommendation is to choose an investment portfolio with {}
                """.format(first_name, recommendation)
        }
    )

def validate(age, investment_amount):
    """
    Validates age and investment_amount
    """
    print(f'DEBUG - VALIDATE - age: {age}, amt: {investment_amount}')
    if age is not None:
        age = parse_int(age)
        if age >= 65:
            return build_validation_result(
                False,
                "age",
                "It's too late, you're screwed! Move in with your kids.")
        elif age < 0:
            return build_validation_result(
                False,
                "age",
                "Invalid age, must be greater than 0 and less than 65.")
                
    if investment_amount is not None:
        investment_amount = parse_float(investment_amount)
        if investment_amount < MIN_INVESTMENT_AMT:
            return build_validation_result(
                False,
                "investmentAmount",
                "The minimum investment amount is $5000.")

    return build_validation_result(True, None, None)

def getRecommendationForRiskLevel(risk_level):
    recommendation = 'Invalid risk level'
    if risk_level == "None":
        recommendation = '100% bonds (AGG), 0% equities (SPY)'
    elif risk_level == "Very Low":
        recommendation = '80% bonds (AGG), 20% equities (SPY)'
    elif risk_level == "Low":
        recommendation = '60% bonds (AGG), 40% equities (SPY)'
    elif risk_level == "Medium":
        recommendation = '40% bonds (AGG), 60% equities (SPY)'
    elif risk_level == "High":
        recommendation = '20% bonds (AGG), 80% equities (SPY)'
    elif risk_level == "Very High":
        recommendation = '0% bonds (AGG), 100% equities (SPY)'
    return recommendation

### Intents Dispatcher ###
def dispatch(intent_request):
    """
    Called when the user specifies an intent for this bot.
    """

    intent_name = intent_request["currentIntent"]["name"]

    # Dispatch to bot's intent handlers
    if intent_name == "RecommendPortfolio":
        return recommend_portfolio(intent_request)

    raise Exception("Intent with name " + intent_name + " not supported")


### Main Handler ###
def lambda_handler(event, context):
    """
    Route the incoming request based on intent.
    The JSON body of the request is provided in the event slot.
    """

    return dispatch(event)
