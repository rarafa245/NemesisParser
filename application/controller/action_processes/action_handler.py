import json
from typing import Dict
from application.db import redis_insert_localization

def parser_action(client, message: Dict) -> bool:
    ''' Filtering the datas and sending to the correct locals
        :parram - client: MQTT Client Connection
                - message: dictionary with the traduced message
        :return boolean with success/failure of all processes
    '''
    

    if message['TYPE'] == b'01':
        # Response to Gateway and DB topic

        response = message["HEADER"] \
                    + message["DEVICE"] \
                    + message["TYPE"] \
                    + b'50494E47' \
                    + message["FOOTER"]

        response_db = {
            "DEVICE": message["DEVICE"].decode('utf8'),
            "TYPE": "PING",
            "DATE_INFO": message["DATE_INFO"]
        }

        json_message = json.dumps(response_db)
    
        client.publish(topic='/ping', payload=response)
        client.publish(topic='/DB', payload=json_message)

        return True

    
    elif message['TYPE'] == b'02':
        # Converting message to Json and storing it in Redis
        # and send it to Gateway to DBexport

        copy_message = message
        copy_message["TYPE"] = "LOC"
        json_message = json.dumps(copy_message)
        ttl = 180

        if message['FIX'] and not message['HIST']:
            # If GPS has FIX and data not historic
            insert_data = redis_insert_localization(message["DEVICE"], json_message, ttl)
        
        client.publish(topic='/DB', payload=json_message)

        return True

    return False
