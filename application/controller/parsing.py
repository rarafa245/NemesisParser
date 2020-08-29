from typing import Dict

def parsing_message(message: bool) -> Dict:

    str_message = str(message).split("'")[1]

    message_header = str_message[:4]
    message_device = str_message[4:10]
    message_type = str_message[10:12]
    message_payload = str_message[12:-4]
    message_footer = str_message[-4:]

    parsed_message = {
        "HEADER":   message_header,
        "DEVICE":   message_device,
        "TYPE":     message_type,
        "PAYLOAD":  message_payload,
        "FOOTER":   message_footer
    }

    return parsed_message


def parsering_message_payload(payload: str):
    pass