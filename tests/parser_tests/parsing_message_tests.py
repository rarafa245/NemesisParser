from application.controller.parser_processes.parsing import parsing_message
import pytest

@pytest.mark.parametrize('message, result',
[
    # Testing normal message location
    (bytearray('50F70A3F73025EFCF950156F017D784000008CA0F8003C013026A1029E72BD73C4', "utf8"), 
        {
            "HEADER": b'50F7',
            "DEVICE": b'0A3F73',
            "TYPE": b'02',
            "PAYLOAD": {
                        "TIMESTAMP": b'5EFCF950',
                        "DIRECTION": b'156F',
                        "DISTANCE": b'017D7840',
                        "TIME_ON": b'00008CA0',
                        "COMPOSER": b'F800',
                        "SPEED": b'3C',
                        "LATITUDE": b'013026A1',
                        "LONGITUDE": b'029E72BD'
                        },
            "FOOTER": b'73C4'
        }
    ),

    # Testing normal message location without payload
    (bytearray('50F70A3F730273C4', "utf8"),     
        {
            "HEADER": b'50F7',
            "DEVICE": b'0A3F73',
            "TYPE": b'02',
            "PAYLOAD": {
                        "TIMESTAMP": b'',
                        "DIRECTION": b'',
                        "DISTANCE": b'',
                        "TIME_ON": b'',
                        "COMPOSER": b'',
                        "SPEED": b'',
                        "LATITUDE": b'',
                        "LONGITUDE": b''
                        },
            "FOOTER": b'73C4'
        }
    ),

    # testing normal message ping
    (bytearray('50F70A3F730150494E4773C4', "utf8"), 
        {
            "HEADER": b'50F7',
            "DEVICE": b'0A3F73',
            "TYPE": b'01',
            "PAYLOAD": b'50494E47',
            "FOOTER": b'73C4'
        }
    ),

    # Testing message with header error
    (bytearray('55F70A3F73025EFCF950156F017D784000008CA0F8003C013026A1029E72BD73C4', "utf8"), 
        {
            "HEADER":   b'0000',
            "DEVICE":   b'000000',
            "TYPE":     b'0',
            "PAYLOAD":  b'',
            "FOOTER":   b'0000'
        }
    ),

    # Testing message with footer error
    (bytearray('50F70A3F73025EFCF950156F017D784000008CA0F8003C013026A1029E72BD77C4', "utf8"), 
        {
            "HEADER":   b'0000',
            "DEVICE":   b'000000',
            "TYPE":     b'0',
            "PAYLOAD":  b'',
            "FOOTER":   b'0000'
        }
    ),

    # Testing message with more caracteres
    (bytearray('150F70A3F73025EFCF950156F017D784000008CA0F8003C013026A1029E72BD73C4', "utf8"), 
        {
            "HEADER":   b'0000',
            "DEVICE":   b'000000',
            "TYPE":     b'0',
            "PAYLOAD":  b'',
            "FOOTER":   b'0000'
        }
    ),

    # Testing message with header and footer error
    (bytearray('50F70A3F73025EFCF950156F017D784000008CA0F8003C013026A1029E72BD73C41', "utf8"), 
        {
            "HEADER":   b'0000',
            "DEVICE":   b'000000',
            "TYPE":     b'0',
            "PAYLOAD":  b'',
            "FOOTER":   b'0000'
        }
    ),
])
def teste_parsing_message(message, result):
    assert parsing_message(message) == result