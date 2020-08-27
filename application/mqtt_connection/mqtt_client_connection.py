import paho.mqtt.client as mqtt
import time
from .client_config import on_connect


class Mqtt_Client:

    def __init__(self, broker_ip: str, port: int, client_id: str, keepalive=60):
        ''' Constructor Method - Create and save the important atributes
            :parram - broker_ip: The adress of the host
                    - port: The port of the broker adress
                    - client_id: A Client name for identification
                    - keepalive: Keepalive of the connectio
        '''
        
        self.broker_ip = broker_ip
        self.client_id = client_id
        self.port = port
        self.mqtt_client = self.start_connection(self.broker_ip, self.client_id, 
                                            self.port, keepalive)


    def start_connection(self, broker_ip: str, client_name: str, port: int, keepalive: int):
        ''' Create a connected client and return it
            :parram - broker_ip: The adress of the host
                    - port: The port of the broker adress
                    - client_id: A Client name for identification
                    - keepalive: Keepalive of the connection
            :return - Client connection
        '''
        
        mqtt_client = mqtt.Client(client_name)
        mqtt_client.on_connect = on_connect

        mqtt_client.connect(host=broker_ip, port=port, keepalive=keepalive)
        mqtt_client.loop_start()
        return mqtt_client


    def end_connection(self):
        ''' Ends the client connection
            :parram - None
            :return - Boolean with the sucess/failure of the process
        '''
        
        try: 
            self.mqtt_client.loop_stop()
            self.mqtt_client.disconnect()

        except:
            return False
        
        return True
        