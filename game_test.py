import pytest

from game import is_exit

def test_is_exit():
    assert is_exit(3) == True
    assert is_exit(-1) == False
    assert is_exit(0) == False
    assert is_exit(1) == False
    assert is_exit(2) == False