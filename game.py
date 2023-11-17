from enum import Enum
from log_error import log_error
from random import choice


class GameChoice(Enum):
    INVALIDE = -1
    ROCK = 0
    PAPER = 1
    SCISSORS = 2
    LIZARD = 3
    SPOCK = 4
    QUIT = 5

def game_loop()->None:

    """
    Arranca el bucle principal del juego
    """
    while True:
        # Leo la selección del usuario (piedra, papel, tijera o parar el juego)
        user_choice = read_user_choice()
        
        # Siempre y cuando no quiera parar
        if not is_exit(user_choice):
            print(f"Has jugado: {user_choice.name} ")
            
            # genero una jugada del ordenador
            comp_choice = generate_computer_choice()
            print(f"El ordenador a jugado: {comp_choice.name}")
           
            # evalúo la jugada
            result = evaluate_move(user_choice, comp_choice)
            # muestro el ganador en pantalla y vuelta al principio
            print_result(result)
        else:
            # el humano es un gallina: salgo
            break

def read_user_choice()-> GameChoice:
    """
    Imprime un menu de instrucciones y lee la respuesta del usuario
    mediante una llamada a `input`.
    Devuelve lo que haya elegido el usario
    """

    user_answer = GameChoice.INVALIDE

    while user_answer == GameChoice.INVALIDE:

        print('Select one option:')
        print(f'{GameChoice.ROCK.value}.- Rock')
        print(f'{GameChoice.PAPER.value}.- Paper')
        print(f'{GameChoice.SCISSORS.value}.- Scissors')
        print(f'{GameChoice.LIZARD.value}. Lagarto')
        print(f'{GameChoice.SPOCK.value}. Spock')
        print('************************')
        print(f'{GameChoice.QUIT.value}. I don´t want play again.')

        try:
            user_answer = GameChoice(int(input('Choice your option: ')))
        except ValueError as err:
            user_answer = GameChoice.INVALIDE
            log_error(err)
            

    return user_answer


def is_exit(user_choice)-> bool:
    """
    Predicado que recibe la espuesta del usuario y devuelve `True` si
    ha pedido salir del juego

    """
    return user_choice == GameChoice.QUIT



def generate_computer_choice()-> GameChoice:
    """
    Genera una jugada del ordenador de forma aleatroia. El ordenador no puede elegir
    para el juego, solo Piedra, Papel o Tijera
    """
    
    return choice([GameChoice.ROCK, GameChoice.PAPER, GameChoice.SCISSORS, GameChoice.LIZARD, GameChoice.SPOCK])

def evaluate_move(user_choice, computer_choice)-> str:
    """
    Recibe dos jugadas, determina cual ha ganado y devuelve un mensaje con el resultado.
    Por ejemplo: recibe Papel y Piedra, y devuelve "Papel envuelve Piedra"
    """
    assert user_choice != GameChoice.INVALIDE and user_choice != GameChoice.QUIT
    assert computer_choice != GameChoice.INVALIDE and computer_choice != GameChoice.QUIT

    winner = {GameChoice.PAPER: [GameChoice.ROCK, GameChoice.SPOCK], 
              GameChoice.ROCK: [GameChoice.SCISSORS, GameChoice.LIZARD],
              GameChoice.SCISSORS:[GameChoice.PAPER, GameChoice.LIZARD],
              GameChoice.LIZARD: [GameChoice.PAPER, GameChoice.SPOCK],
              GameChoice.SPOCK: [GameChoice.ROCK, GameChoice.SCISSORS]}
   
    result = ""
    if user_choice == computer_choice:
        result = "You tie!!!!"
    elif computer_choice in winner[user_choice]:
        result = "YOU WINN!!!!"
    else:
        result = "YOU LOSE!!!!"

    assert result != ""
    return result



def print_result(result)-> None:
    """
    Imprime en plan bonito el resultado.
    No devuelve nada
    """
    print("GAME IS OVER!!!!")
    print(result)
    print("***************")


if __name__ == "__main__":
    try:
        game_loop()
    except Exception as error:
        log_error(error)
        print(error)
