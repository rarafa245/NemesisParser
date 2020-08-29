from typing import Dict

def parsing_message(message: str) -> Dict:
    ''' Recive a message and parser it
        :parram - message: bytearray with the received message
        :return - dictionary with the parsed message
    '''

    message_header = message[:4]
    message_footer = message[-4:]
    
    valid_message = consistency_checker(message_header, message_footer)

    if valid_message:
        message_device = message[4:10]
        message_type = message[10:12]
        message_payload = message[12:-4]
        
        parsed_message = {
            "HEADER":   message_header,
            "DEVICE":   message_device,
            "TYPE":     message_type,
            "PAYLOAD":  message_payload,
            "FOOTER":   message_footer
        }

    else:
        parsed_message = {
            "HEADER":   b'0000',
            "DEVICE":   b'000000',
            "TYPE":     b'0',
            "PAYLOAD":  b'',
            "FOOTER":   b'0000'
        }

    return parsed_message


def consistency_checker(header: str, footer: str) -> bool:
    ''' Check if the header and the footer of the message are consistency
        :parram - header: First 2 bytes of the message
                - footer: Last 2 bytes of the message
        :return - boolean with the sucess/faluir of the check 
    '''

    consistency_header = b'50F7'
    consistency_footer = b'73C4'

    if (header != consistency_header) or (footer != consistency_footer):
        return False

    return True
