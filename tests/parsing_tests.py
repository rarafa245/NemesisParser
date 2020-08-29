from application.controller.parsing import parsing_message
import pytest

@pytest.mark.parametrize('message, result',
[
    (bytearray('50F70A3F73025EFCF950156F017D784000008CA0F80084003C013026A1029E72BD73C4', "utf8"), 
        {
            "HEADER": "50F7",
            "DEVICE": "0A3F73",
            "TYPE": "02",
            "PAYLOAD": "5EFCF950156F017D784000008CA0F80084003C013026A1029E72BD",
            "FOOTER": "73C4"
        }
    ),

    (bytearray('50F70A3F730273C4', "utf8"), 
        {
            "HEADER": "50F7",
            "DEVICE": "0A3F73",
            "TYPE": "02",
            "PAYLOAD": "",
            "FOOTER": "73C4"
        }
    ),

    (bytearray('50F70A3F730150494E4773C4', "utf8"), 
        {
            "HEADER": "50F7",
            "DEVICE": "0A3F73",
            "TYPE": "01",
            "PAYLOAD": "50494E47",
            "FOOTER": "73C4"
        }
    ),
    

])
def teste_parsing_message(message, result):
    assert parsing_message(message) == result