from application.controller.parsing import consistency_checker
import pytest

@pytest.mark.parametrize('header, footer, result',
[
    (b'50F7', b'73C4', True),
    (b'50F3', b'73C4', False),
    (b'50F3', None, False),
    (None, None, False),
    (b'50F7', b'72C8', False),
    (b'30F2', b'72C8', False),

])
def teste_parsing_message(header, footer, result):
    assert consistency_checker(header, footer) == result
