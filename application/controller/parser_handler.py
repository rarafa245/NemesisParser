from .parser_processes import parsing_message
from .traducer_processes import traducing_message_location, traducing_message_ping
from .action_processes import parser_action



def on_received_message(client, message: bytearray) -> bool:
    ''' Callback function to process the received message:
            Parsing, Traducing, Acting
        :parram - client: MQTT Client Connection
                - message: raw message in bytearray
        :return boolean with success/failure of all processes
    '''

    parsed_messsage = {}
    traduced_message = {}

    # Parsing
    parsed_messsage = parsing_message(message)

    # Traducing
    if parsed_messsage["TYPE"] == b'02':
        traduced_message = traducing_message_location(parsed_messsage)
    elif parsed_messsage["TYPE"] == b'01':
        traduced_message = traducing_message_ping(parsed_messsage)
    
    # Acting
    send_response = parser_action(client, traduced_message)

    return send_response
