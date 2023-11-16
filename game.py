from enum import Enum
from log_error import log_error
from random import choice

class UserChoice(Enum):
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

    user_answer = UserChoice.INVALIDE

    while True:

        print('Select one option:')
        print(f'{UserChoice.ROCK.value}.- Rock')
        print(f'{UserChoice.PAPER.value}.- Paper')
        print(f'{UserChoice.SCISSORS.value}.- Scissors')
        print('************************')
        print(f'{UserChoice.QUIT.value}. I don´t want play again')

        try:
            user_answer = int(input('Choice your option: '))
        except ValueError as err:
            user_answer = UserChoice.INVALIDE
            log_error(err)
            print(err)

        if user_answer != UserChoice.INVALIDE:
            break
        else:
            user_answer = UserChoice.INVALIDE

    return user_answer


def is_exit(user_choice):
    """
    Predicado que recibe la espuesta del usuario y devuelve `True` si
    ha pedido salir del juego

    """
    return user_choice == UserChoice.QUIT.value



def generate_computer_choice():
    """
    Genera una jugada del ordenador de forma aleatroia. El ordenador no puede elegir
    para el juego, solo Piedra, Papel o Tijera
    """
    return choice([UserChoice.ROCK.value, UserChoice.PAPER.value, UserChoice.SCISSORS.value])

def evaluate_move(user_choice, computer_choice):
    """
    Recibe dos jugadas, determina cual ha ganado y devuelve un mensaje con el resultado.
    Por ejemplo: recibe Papel y Piedra, y devuelve "Papel envuelve Piedra"
    """
    assert user_choice != UserChoice.INVALIDE and user_choice != UserChoice.QUIT
    assert computer_choice != UserChoice.INVALIDE and computer_choice != UserChoice.QUIT

    result = ""
    if user_choice == UserChoice.ROCK.value:
        if computer_choice == UserChoice.PAPER.value:
            result = "You lose!!! Paper wins rock."
        elif computer_choice == UserChoice.SCISSORS.value:
            result = "YOU WIN!!!! Rock wins Scissors."
        elif computer_choice == UserChoice.ROCK.value:
            result = "You tie!!!!"
    elif user_choice == UserChoice.PAPER.value:
        if computer_choice == UserChoice.ROCK.value:
            result = "YOU WIN!!! Paper wins Rock"
        elif computer_choice == UserChoice.SCISSORS.value:
            result = "You lose!!! Scissors wins Paper"
        else:
            result = "You tie!!!!"
    elif user_choice == UserChoice.SCISSORS.value:
        if computer_choice == UserChoice.PAPER.value:
            result = "YOU WIN!!! Scissors wins Paper."
        elif computer_choice == UserChoice.ROCK.value:
            result = "You lose!!! Rock wins Scissors."
        else:
            result = "You tie!!!!"


    return result

def print_result(result):
    """
    Imprime en plan bonito el resultado.
    No devuelve nada
    """
    return None # pa que te calles!


if __name__ == "__main__":
    try:
        game_loop()
    except Exception as error:
        log_error(error)
        print(error)
