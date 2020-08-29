def parsing_payload(message_payload):

    timestamp = message_payload[:8]
    direction = message_payload[8:12]
    distance = message_payload[12:20]
    time_on = message_payload[20:28]
    composer = message_payload[28:32]
    speed = message_payload[32:34]
    latitude = message_payload[34:42]
    longitude = message_payload[42:50]

    parsed_payload = {
        "TIMESTAMP":    timestamp,
        "DIRECTION":    direction,
        "DISTANCE":     distance,
        "TIME_ON":      time_on,
        "COMPOSER":     composer,
        "SPEED":        speed,
        "LATITUDE":     latitude,
        "LONGITUDE":    longitude
    }
    
    return parsed_payload