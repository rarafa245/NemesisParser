from typing import Dict
from application.mqtt_connection import ParserClient

def publish_message(topic: str, message: Dict) -> None:
    ''' Publish a message in a certain topic
        :param: - topic: MQTT topic of the publish
                - message: Message to publish
        :return - None
    '''

    ParserClient.mqtt_client.publish(topic=topic, payload=message)
