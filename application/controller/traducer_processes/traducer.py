from typing import Dict, Tuple
from collections import namedtuple
import datetime


def traducing_message(message: Dict) -> Dict:
    ''' Processing some funtionalitys to traduce the message
        :parram: message - a dictionary with all the parsed informations
        :return: traduced_data - a dictionary with traduced informations
    '''
    
    # Getting relevant initial informations
    GPS_precision = 1000000
    distance_convert_km = 1000
    payload = message["PAYLOAD"]
    message_type = message["TYPE"]
    device = message["DEVICE"].decode('utf8')

    
    # Converting payload elements in int
    timestamp = int(payload["TIMESTAMP"], 16)
    angle = int(payload["DIRECTION"], 16)         
    distance = int(payload["DISTANCE"], 16) / distance_convert_km
    time_on = int(payload["TIME_ON"], 16)         
    speed = int(payload["SPEED"], 16)             
    latitude = int(payload["LATITUDE"], 16) / (GPS_precision)
    longitude = int(payload["LONGITUDE"], 16) / (GPS_precision)
    composer = int(payload["COMPOSER"], 16)

    # Get data values from timestamp
    date_values = convert_timestamp_to_date(timestamp)

    # Getting Composer Infos and changing Lat, Long signal
    composer_infos = check_composer(composer)
    if composer_infos.lat_negative: latitude = (-1) * latitude
    if composer_infos.lon_negative: longitude = (-1) * longitude

    # Defining informations of fix, live gps and ignition
    fix = composer_infos.fix
    live = composer_infos.live
    ignition = composer_infos.ignition

    traduced_data = {
        "DEVICE": device,
        "TYPE": message_type,
        "FIX": fix,
        "LIVE": live,
        "IGNITION": ignition,
        "DATE_INFOS": date_values,
        "ANGLE": angle,
        "DISTANCE": distance,
        "TIME_ON": time_on,
        "SPEED": speed,
        "LATITUDE": latitude,
        "LONGITUDE": longitude,
    }

    return traduced_data


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