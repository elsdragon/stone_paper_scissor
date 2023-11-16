import pytest

from game import generate_computer_choice, is_exit

def test_is_exit():
    assert is_exit(3) == True
    assert is_exit(-1) == False
    assert is_exit(0) == False
    assert is_exit(1) == False
    assert is_exit(2) == False

def test_generate_computer_choice():
    assert generate_computer_choice() == 0 or 1 or 2