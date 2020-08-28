from typing import Dict

def parsing_message(message: bool) -> Dict:

    str_message = str(message).split("'")[1]

    message_header = str_message[:4]
    message_type = str_message[4:10]
    message_payload = str_message[10:-4]
    message_footer = str_message[-4:]


def parsering_message_payload(payload: str):
    pass