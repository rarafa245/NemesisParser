from .parser_processes import parsing_message
from .traducer_processes import traducing_message


def on_received_message(message: str):

    # Parsing
    parsed_messsage = parsing_message(message)

    # Traducing
    if parsed_messsage["TYPE"] == b'02':
        traducing_message(parsed_messsage)

    # Acting


    return parsed_messsage
    