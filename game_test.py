import pytest

from game import evaluate_move, generate_computer_choice, is_exit

def test_is_exit():
    assert is_exit(3) == True
    assert is_exit(-1) == False
    assert is_exit(0) == False
    assert is_exit(1) == False
    assert is_exit(2) == False

def test_generate_computer_choice():
    assert generate_computer_choice() == 0 or 1 or 2

def test_evaluate_move():
    assert evaluate_move(0, 0) == "You tie!!!!"
    assert evaluate_move(1, 1) == "You tie!!!!"
    assert evaluate_move(2, 2) == "You tie!!!!"
    assert evaluate_move(0, 1) == "You lose!!! Paper wins rock."
    assert evaluate_move(0, 2) == "YOU WIN!!!! Rock wins Scissors."
    assert evaluate_move(1, 0) == "YOU WIN!!! Paper wins Rock"
    assert evaluate_move(1, 2) == "You lose!!! Scissors wins Paper"
    assert evaluate_move(2, 1) == "YOU WIN!!! Scissors wins Paper."
    assert evaluate_move(2, 0) == "You lose!!! Rock wins Scissors."
   