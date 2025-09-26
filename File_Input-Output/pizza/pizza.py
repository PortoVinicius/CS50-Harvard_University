import sys
import csv
from tabulate import tabulate


def main():
    with open("regular.csv", "r") as file:
        reader = csv.reader(file)
        print(tabulate(reader))


if __name__ == "__main__":
    main()