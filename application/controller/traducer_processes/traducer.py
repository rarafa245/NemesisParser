from typing import Dict
import datetime


def traducing_message(message: Dict) -> Dict:
    
    # Getting relevant initial informations
    message_type = 'loc'
    payload = message['PAYLOAD']
    
    # Converting payload elements in int
    timestamp = int(payload["TIMESTAMP"], 16)
    angle = int(payload["DIRECTION"], 16)         
    distance = int(payload["DISTANCE"], 16)
    time_on = int(payload["TIME_ON"], 16)         
    speed = int(payload["SPEED"], 16)             
    raw_latitude = int(payload["LATITUDE"], 16)       # form
    raw_longitude = int(payload["LONGITUDE"], 16)     # form
    composer = int(payload["COMPOSER"], 16)

    # Get data values from timestamp
    date_values = convert_timestamp_to_date(timestamp)

    # Passing distance m - km
    distance_km = distance/1000
    

def check_composer():
    pass


def convert_timestamp_to_date(timestamp: int) -> Dict:
    ''' Converting timestamp in date values
        :parram - timestamp: timestamp int
        :return - dictionary with data and start time of timestamp
    '''

    date_information = datetime.datetime.fromtimestamp(timestamp)
    date = date_information.strftime('%Y-%m-%d')
    start_time = date_information.strftime('%Y-%m-%d %H:%M:%S')

    date_values = {
        "DATE": date,
        "START_TIME": start_time
    }

    return date_values


def check_bit(byte_info: int, position: int) -> bool:
    ''' Using bitmask, checking the value (0/1) of the bit
        :parram - byte_info: byte information converting in int
                - position: position of the check (start with 0)
        :return - boolean False/True (0/1)
    '''
    
    if byte_info & (1 << position):
        return True

    return False