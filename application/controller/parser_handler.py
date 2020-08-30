from .parser_processes import parsing_message
from .traducer_precesses import traducing_message


def on_received_message(message: str):


    parsed_messsage = parsing_message(message)

    if parsed_messsage["TYPE"] == b'02':
        traducing_message(parsed_messsage)

    return parsed_messsage
    