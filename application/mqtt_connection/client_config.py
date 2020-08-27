mqtt_client_config = {
    "BROKER" : "localhost",
    "CLIENT_NAME": "NemesisParser",
    "PORT": 1883,
    "KEEPALIVE": 60
}


def on_connect(client, userdata, flags, rc):
    print(client)