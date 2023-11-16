import logging

# Crea un archivo de registro y establece el nivel de registro a DEBUG


def log_error(error):
    logging.basicConfig(filename='mi_programa.log', level=logging.DEBUG)
    logging.exception("Ocurrió una excepción")
    print(error)