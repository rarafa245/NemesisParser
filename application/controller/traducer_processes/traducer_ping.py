from datetime import datetime
from typing import Dict

def traducing_message_ping(message: Dict) -> Dict:
    ''' Processing some funtionalitys to traduce the message
        :parram: message - a dictionary with all the parsed informations
        :return: traduced_data - a dictionary with traduced informations
    '''

    header = message["HEADER"]
    footer = message["FOOTER"]
    message_type = message["TYPE"]
    device = message["DEVICE"]
    date_info = get_current_date()

    traduced_data = {
        "HEADER": header,
        "DEVICE": device,
        "TYPE": message_type,
        "DATE_INFO": date_info,
        "FOOTER": footer
    }
    
    return traduced_data


def get_current_date() -> Dict:
    ''' Return informations of the current date
        :parram - None
        :return - Dictionary with some date informations
    '''

    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    start_time = now.strftime("%Y-%m-%d %H:%M:%S")

    date_info = {
        "DATE": date,
        "START_TIME": start_time
    }

    return date_info