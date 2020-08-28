import paho.mqtt.client as mqtt
import time
from .client_callbacks import on_connect, on_subscribe, on_disconnect, on_message


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
        self.keepalive = keepalive
        self.mqtt_client = self.start_connection(self.broker_ip, self.client_id, 
                                                self.port, self.keepalive)


    def start_connection(self, broker_ip: str, client_name: str, port: int, keepalive: int):
        ''' Create a connected client and return it
            :parram - broker_ip: The adress of the host
                    - port: The port of the broker adress
                    - client_id: A Client name for identification
                    - keepalive: Keepalive of the connection
            :return - Client connection
        '''
        
        mqtt_client = mqtt.Client(client_name)
        mqtt_client.on_connect = on_connect                                 # Defining callback connect to MQTT Broker
        mqtt_client.on_subscribe = on_subscribe                             # Defining callback Subscribe Topic
        mqtt_client.on_disconnect = on_disconnect                           # Defining callback Disconnect to MQTT Broker
        mqtt_client.on_message = on_message                                 # Defining callback Receving Message from Subscribe

        mqtt_client.connect(host=broker_ip, port=port, keepalive=keepalive)
        mqtt_client.loop_start()                                            # Starting Event Loop for callbacks
        
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
    
    def get_mqtt_client(self):
        ''' Getting mqtt client connection
            :parram - None
            :return - mqtt_client
        '''

        return self.mqtt_client
        