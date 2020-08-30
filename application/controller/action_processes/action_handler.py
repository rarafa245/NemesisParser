import json
from typing import Dict
from application.db import redis_client

def parser_action(client, message: Dict): 
    
    #print(message)
    copy_message = message

    if message['TYPE'] == b'01':
        # Response to Gateway and DB topic

        response = message['HEADER'] \
                    + message["DEVICE"] \
                    + message["TYPE"] \
                    + b'50494E47' \
                    + message["FOOTER"]

        client.publish(topic='/ping', payload=response)
        client.publish(topic='/DB', payload=response)
    
    elif message['TYPE'] == b'02':
        # Converting message to Json and storing it in Redis
        # and send it to Gateway to DBexport

        copy_message["TYPE"] = "LOC"
        json_message = json.dumps(copy_message)

        redis_client.set('message', json_message, ex=60)
    
    else:
        #Response to Nowhere
        print('erro all message')