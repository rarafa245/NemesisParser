from application.controller.parser_handler import on_received_message
import pytest

@pytest.mark.parametrize('message, result',
[
    (bytearray('50F70A3F73025EFCF950156F017D784000008CA0F80084003C013026A1029E72BD73C4', "utf8"), 
        {
            "HEADER": b'50F7',
            "DEVICE": b'0A3F73',
            "TYPE": b'02',
            "PAYLOAD": b'5EFCF950156F017D784000008CA0F80084003C013026A1029E72BD',
            "FOOTER": b'73C4'
        }
    ),

    (bytearray('50F70A3F730273C4', "utf8"), 
        {
            "HEADER": b'50F7',
            "DEVICE": b'0A3F73',
            "TYPE": b'02',
            "PAYLOAD": b'',
            "FOOTER": b'73C4'
        }
    ),

    (bytearray('50F70A3F730150494E4773C4', "utf8"), 
        {
            "HEADER": b'50F7',
            "DEVICE": b'0A3F73',
            "TYPE": b'01',
            "PAYLOAD": b'50494E47',
            "FOOTER": b'73C4'
        }
    ),

    (bytearray('55F70A3F73025EFCF950156F017D784000008CA0F80084003C013026A1029E72BD73C4', "utf8"), 
        {
            "HEADER":   b'0000',
            "DEVICE":   b'000000',
            "TYPE":     b'0',
            "PAYLOAD":  b'',
            "FOOTER":   b'0000'
        }
    ),

    (bytearray('50F70A3F73025EFCF950156F017D784000008CA0F80084003C013026A1029E72BD77C4', "utf8"), 
        {
            "HEADER":   b'0000',
            "DEVICE":   b'000000',
            "TYPE":     b'0',
            "PAYLOAD":  b'',
            "FOOTER":   b'0000'
        }
    ),

    (bytearray('150F70A3F73025EFCF950156F017D784000008CA0F80084003C013026A1029E72BD73C4', "utf8"), 
        {
            "HEADER":   b'0000',
            "DEVICE":   b'000000',
            "TYPE":     b'0',
            "PAYLOAD":  b'',
            "FOOTER":   b'0000'
        }
    ),

    (bytearray('50F70A3F73025EFCF950156F017D784000008CA0F80084003C013026A1029E72BD73C41', "utf8"), 
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
    assert on_received_message(message) == result