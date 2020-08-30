from .parser_processes import parsing_message
from .traducer_processes import traducing_message


def on_received_message(message: str):

    parsed_messsage = {}
    traduced_message = {}

    # Parsing
    parsed_messsage = parsing_message(message)

    # Traducing
    if parsed_messsage["TYPE"] == b'02':
        traduced_message = traducing_message(parsed_messsage)
    else:
        traduced_message = parsed_messsage
    
    print(traduced_message)
    # Acting


    return parsed_messsage
    