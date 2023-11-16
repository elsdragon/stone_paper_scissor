import pytest

from game import evaluate_move, generate_computer_choice, is_exit, GameChoice

def test_is_exit():
    assert is_exit(3) == True
    assert is_exit(-1) == False
    assert is_exit(0) == False
    assert is_exit(1) == False
    assert is_exit(2) == False

def test_generate_computer_choice():
    assert generate_computer_choice() == 0 or 1 or 2

def test_evaluate_move():
    assert evaluate_move(GameChoice.ROCK, GameChoice.ROCK) == "You tie!!!!"
    assert evaluate_move(GameChoice.PAPER, GameChoice.PAPER) == "You tie!!!!"
    assert evaluate_move(GameChoice.SCISSORS, GameChoice.SCISSORS) == "You tie!!!!"
    assert evaluate_move(GameChoice.ROCK, GameChoice.PAPER) == "You lose!!! Paper wins rock."
    assert evaluate_move(GameChoice.ROCK, GameChoice.SCISSORS) == "YOU WIN!!!! Rock wins Scissors."
    assert evaluate_move(GameChoice.PAPER, GameChoice.ROCK) == "YOU WIN!!! Paper wins Rock"
    assert evaluate_move(GameChoice.PAPER, GameChoice.SCISSORS) == "You lose!!! Scissors wins Paper"
    assert evaluate_move(GameChoice.SCISSORS, GameChoice.PAPER) == "YOU WIN!!! Scissors wins Paper."
    assert evaluate_move(GameChoice.SCISSORS, GameChoice.ROCK) == "You lose!!! Rock wins Scissors."
   