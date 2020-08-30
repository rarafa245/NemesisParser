from typing import Dict
from application.db import redis_client

def parser_action(client, message: Dict): 
    
    print(message)
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
        # Response to Redis and DB

        print('local message')
    
    else:
        #Response to Nowhere
        print('erro all message')