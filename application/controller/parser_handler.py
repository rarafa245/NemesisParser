from .parser_processes import parsing_message

def on_received_message(message: str):

    return parsing_message(message)
    