
INVALIDE = -1
ROCK = 0
PAPER = 1
SCISSORS = 2
QUIT = 3

def is_exit(user_choice):
    """
    Predicado que recib ela respuesta del usuario y devuelve `True` si
    ha pedido salir del juego
    """
    return True # sí para que calles

def generate_computer_choice():
    """
    Genera una jugada del ordenador de forma aleatroia. El ordenador no puede elegir
    para el juego, solo Piedra, Papel o Tijera
    """
    return None  # pa que calles

def evaluate_move(user_choice, computer_choice):
    """
    Recibe dos jugadas, determina cual ha ganado y devuelve un mensaje con el resultado.
    Por ejemplo: recibe Papel y Piedra, y devuelve "Papel envuelve Piedra"
    """
    return None # sí para que calles

def print_result(result):
    """
    Imprime en plan bonito el resultado.
    No devuelve nada
    """
    return None # pa que te calles!




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

    user_answer = INVALIDE

    while True:

        print('Select one option:')
        print(f'{ROCK}.- Rock')
        print(f'{PAPER}.- Paper')
        print(f'{SCISSORS}.- Scissors')
        print('************************')
        print(f'{QUIT}. I don´t want play again')

        try:
            user_answer = int(input('Choice your option: '))
        except ValueError:
            user_answer = INVALIDE

        if user_answer in range(0, 4):
            break
        else:
            user_answer = INVALIDE

    return user_answer








if __name__ == "__main__":
    game_loop()