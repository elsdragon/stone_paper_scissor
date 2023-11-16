from enum import Enum
from log_error import log_error


class GameChoice(Enum):
    INVALIDE = -1
    ROCK = 0
    PAPER = 1
    SCISSORS = 2
    QUIT = 3

def game_loop():

    """
    Arranca el bucle principal del juego
    """
    while True:
        # Leo la selección del usuario (piedra, papel, tijera o parar el juego)
        user_choice = read_user_choice()
        # Siempre y cuando no quiera parar
        if not is_exit(user_choice):
            # genero una jugada del ordenador
            comp_choice = generate_computer_choice()
            # evalúo la jugada
            result = evaluate_move(user_choice, comp_choice)
            # muestro el ganador en pantalla y vuelta al principio
            print_result(result)
        else:
            # el humano es un gallina: salgo
            break

def read_user_choice():
    """
    Imprime un menu de instrucciones y lee la respuesta del usuario
    mediante una llamada a `input`.
    Devuelve lo que haya elegido el usario
    """

    user_answer = GameChoice.INVALIDE

    while True:

        print('Select one option:')
        print(f'{GameChoice.ROCK.value}.- Rock')
        print(f'{GameChoice.PAPER.value}.- Paper')
        print(f'{GameChoice.SCISSORS.value}.- Scissors')
        print('************************')
        print(f'{GameChoice.QUIT.value}. I don´t want play again\n')

        try:
            user_answer = GameChoice(int(input('Choice your option: ')))
        except ValueError as err:
            user_answer = GameChoice.INVALIDE
            log_error(err)
            

        if user_answer != GameChoice.INVALIDE:
            break
        else:
            user_answer = GameChoice.INVALIDE

    return user_answer


def is_exit(user_choice):
    """
    Predicado que recibe la espuesta del usuario y devuelve `True` si
    ha pedido salir del juego

    """
    return user_choice == GameChoice.QUIT



def generate_computer_choice():
    """
    Genera una jugada del ordenador de forma aleatroia. El ordenador no puede elegir
    para el juego, solo Piedra, Papel o Tijera
    """
    from random import choice
    return choice([GameChoice.ROCK, GameChoice.PAPER, GameChoice.SCISSORS])

def evaluate_move(user_choice, computer_choice):
    """
    Recibe dos jugadas, determina cual ha ganado y devuelve un mensaje con el resultado.
    Por ejemplo: recibe Papel y Piedra, y devuelve "Papel envuelve Piedra"
    """
    assert user_choice != GameChoice.INVALIDE and user_choice != GameChoice.QUIT
    assert computer_choice != GameChoice.INVALIDE and computer_choice != GameChoice.QUIT

    result = ""
    if user_choice == GameChoice.ROCK:
        if computer_choice == GameChoice.PAPER:
            result = "You lose!!! Paper wins rock."
        elif computer_choice == GameChoice.SCISSORS:
            result = "YOU WIN!!!! Rock wins Scissors."
        elif computer_choice == GameChoice.ROCK:
            result = "You tie!!!!"
    elif user_choice == GameChoice.PAPER:
        if computer_choice == GameChoice.ROCK:
            result = "YOU WIN!!! Paper wins Rock"
        elif computer_choice == GameChoice.SCISSORS:
            result = "You lose!!! Scissors wins Paper"
        elif computer_choice == GameChoice.PAPER:
            result = "You tie!!!!"
    elif user_choice == GameChoice.SCISSORS:
        if computer_choice == GameChoice.PAPER:
            result = "YOU WIN!!! Scissors wins Paper."
        elif computer_choice == GameChoice.ROCK:
            result = "You lose!!! Rock wins Scissors."
        elif computer_choice == GameChoice.SCISSORS:
            result = "You tie!!!!"

    assert result != ""
    return result

def print_result(result):
    """
    Imprime en plan bonito el resultado.
    No devuelve nada
    """
    print("GAME IS OVER!!!!\n")
    print(result)
    print("***************")


if __name__ == "__main__":
    try:
        game_loop()
    except Exception as error:
        log_error(error)
        print(error)
