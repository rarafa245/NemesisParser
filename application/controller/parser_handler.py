from .parser_processes import parsing_message

def on_received_message(message: str):


    parsed_messsage = parsing_message(message)
    print(parsed_messsage)
    return parsed_messsage
    