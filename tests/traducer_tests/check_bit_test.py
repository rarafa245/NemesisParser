from application.controller.traducer_processes.traducer import check_bit
import pytest

@pytest.mark.parametrize('byte_info, position, result',
[
    (10, 0, False), # D'10' = 1010
    (11, 0, True),  # D'11' = 1011
    (12, 3, True),  # D'14' = 1100
    (12, 1, False)  # D'14' = 1100
])
def teste_check_bit(byte_info, position, result):
    assert check_bit(byte_info, position) == result
