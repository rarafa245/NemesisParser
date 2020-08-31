from .parser_processes import parsing_message
from .traducer_processes import traducing_message_location, traducing_message_ping
from .action_processes import parser_action



def on_received_message(client, message: str):

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
    parser_action(client, traduced_message)

    return
