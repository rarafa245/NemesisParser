from typing import Dict

def parser_action(client, message: Dict): 
    
    print(message)


    if message['TYPE'] == b'01':
        client.publish(topic='/ola', payload='OOOLA MUNDO')
        
    
    elif message['TYPE'] == b'02':
        print('local message')
    
    else:
        print('erro all message')