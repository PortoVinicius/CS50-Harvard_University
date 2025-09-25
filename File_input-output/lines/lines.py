"""
This program takes the name of a Python file as a command-line argument, counts the number of actual lines of code in that file, and prints the total. 
It excludes comments and blank lines from the count.

Usage:
1. Run the program with the name (or path) of a .py file as a command-line argument.
2. The program will read the file, ignoring blank lines and lines that contain only comments.
3. It will print the number of actual lines of code.

Example:
$ python lines.py text.py ==> Este comando conta quantas linha de codigo existem no programa, sem contar comentarios e linhas vazias
Lines of code: NO momento escrevendo o programa, depois que ele funcionar eu te conto quantals linha de codigo existem
"""

import sys
import csv


def main():
    # Este bloco de codigo verifica o tamanho da len() dos nomes das pastas usadas argumentos 
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1].endswith(".py"):
        
        # Faz a contagem de linhas de codigo no programa text.py
        try:
            with open(sys.argv[1], "r") as file:
                reader = csv.DictReader(file)
                print(reader)
        
        except FileNotFoundError:
            # Imprime uma mensagem informando que o arquivo não é um arquivo em python .py
            sys.exit("File does not exist")

    else:
        # Imprime que o imput inserido como argument não é um arquivo valido
        sys.exit("Not a Python file")


if __name__ == "__main__":
    main()