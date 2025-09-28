# say hello


def main():

    name = input("Whath's your name? ")
    number = int(input("Digite numero: "))

    
    if is_even(number):
        print(f"{number} é um numero divisivel por 2 {name}")
    else:
        print(f"pegar {number} e dividir por 2 vai dar um numero quebrado.")


def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


main()
