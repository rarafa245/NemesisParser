from typing import Dict


def traducing_message(message: Dict) -> Dict:
    
    # Getting relevant initial informations
    message_type = 'loc'
    payload = message['PAYLOAD']
    
    # Converting payload elements in int
    raw_timestamp = int(payload["TIMESTAMP"], 16)     # form
    angle = int(payload["DIRECTION"], 16)         
    distance = int(payload["DISTANCE"], 16)       # form metros - km
    time_on = int(payload["TIME_ON"], 16)         
    speed = int(payload["SPEED"], 16)             
    raw_latitude = int(payload["LATITUDE"], 16)       # form
    raw_longitude = int(payload["LONGITUDE"], 16)     # form

    composer = payload["COMPOSER"]


def check_composer():
    pass


def check_bit(byte, position):
    pass