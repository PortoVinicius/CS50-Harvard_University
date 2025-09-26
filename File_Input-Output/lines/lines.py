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
    elif len(sys.argv) == 2:

        try:
            data = sys.argv[1]
            count = 0

            # Conta quantas linha de codigo validas no prohrama text.py
            if data.endswith(".py"):
                with open(data, "r") as file:
                    for line in file:
                        if line.strip() == "" or line.strip().startswith("#"):
                            pass 
                        else:
                            count += 1
                    print(count)
            
            else:
                sys.exit("Not a Python file")

        except FileNotFoundError:
            # Retorna erro caso não exista arquivo dentro da pasta lines
            sys.exit("File does not exist")


if __name__ == "__main__":
    main()