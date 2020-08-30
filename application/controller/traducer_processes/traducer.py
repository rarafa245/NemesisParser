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

    composer = int(payload["COMPOSER"], 16)


def check_composer():
    pass


def check_bit(byte_info: int, position: int) -> bool:
    ''' Using bitmask, checking the value (0/1) of the bit
        :parram - byte_info: byte information converting in int
                - position: position of the check (start with 0)
        :return - boolean False/True (0/1)
    '''
    
    if byte_info & (1 << position):
        return True

    return False