from typing import Dict, Tuple
from collections import namedtuple
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

    # Getting Composer Infos
    composer_infos = check_composer(composer)

    print(composer_infos)
    print(composer_infos.fix)



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


def check_composer(composer: int) -> Tuple:
    ''' Checking all the bits from composer and returning info
        :parram - composer: integer with especific inforations
        :return - named tuple with informations in the composer
    '''

    # offset to go to most significant byte
    offset = 10
    Composer_Infos = namedtuple('Composer_Infos', 'fix live ignition lat_negative lon_negative')

    # Testing bit 1 - 5 in composer
    fix = check_bit(composer, offset + 5)
    live = check_bit(composer, offset + 4)
    ignition = check_bit(composer, offset + 3)
    lat_negative = check_bit(composer, offset + 2)
    lon_negative = check_bit(composer, offset + 1)

    return Composer_Infos(
        fix = fix,
        live = live,
        ignition = ignition,
        lat_negative = lat_negative,
        lon_negative = lon_negative
    )



def check_bit(byte_info: int, position: int) -> bool:
    ''' Using bitmask, checking the value (0/1) of the bit
        :parram - byte_info: byte information converting in int
                - position: position of the check (start with 0)
        :return - boolean False/True (0/1)
    '''
    
    if byte_info & (1 << position):
        return True

    return False