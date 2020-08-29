from application.controller.parser_processes.payload_processes import parsing_payload
import pytest

@pytest.mark.parametrize('message, result',
[
    (bytearray('5EFCF950156F017D784000008CA0F8003C013026A1029E72BD', "utf8"), 
        {
            "TIMESTAMP": b'5EFCF950',
            "DIRECTION": b'156F',
            "DISTANCE": b'017D7840',
            "TIME_ON": b'00008CA0',
            "COMPOSER": b'F800',
            "SPEED": b'3C',
            "LATITUDE": b'013026A1',
            "LONGITUDE": b'029E72BD'
        }
    ),
])
def teste_parsing_message(message, result):
    assert parsing_payload(message) == result
