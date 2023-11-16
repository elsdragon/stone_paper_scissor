import pytest

from game import evaluate_move, generate_computer_choice, is_exit, GameChoice

def test_is_exit():
    assert is_exit(GameChoice.QUIT) == True
    assert is_exit(GameChoice.INVALIDE) == False
    assert is_exit(GameChoice.ROCK) == False
    assert is_exit(GameChoice.PAPER) == False
    assert is_exit(GameChoice.SCISSORS) == False

def test_generate_computer_choice():
    assert generate_computer_choice() == 0 or 1 or 2

def test_evaluate_move():
    assert evaluate_move(GameChoice.ROCK, GameChoice.ROCK) == "You tie!!!!"
    assert evaluate_move(GameChoice.PAPER, GameChoice.PAPER) == "You tie!!!!"
    assert evaluate_move(GameChoice.SCISSORS, GameChoice.SCISSORS) == "You tie!!!!"
    assert evaluate_move(GameChoice.ROCK, GameChoice.PAPER) == "YOU LOSE!!!!"
    assert evaluate_move(GameChoice.ROCK, GameChoice.SCISSORS) == "YOU WINN!!!!"
    assert evaluate_move(GameChoice.PAPER, GameChoice.ROCK) == "YOU WINN!!!!"
    assert evaluate_move(GameChoice.PAPER, GameChoice.SCISSORS) == "YOU LOSE!!!!"
    assert evaluate_move(GameChoice.SCISSORS, GameChoice.PAPER) == "YOU WINN!!!!"
    assert evaluate_move(GameChoice.SCISSORS, GameChoice.ROCK) == "YOU LOSE!!!!"
   