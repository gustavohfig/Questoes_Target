def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def main():
    n = int(input("Digite um número: "))
    if fibonacci(n) == n:
        print("O número {} pertence à sequência de Fibonacci".format(n))
    else:
        print("O número {} não pertence à sequência de Fibonacci".format(n))


if __name__ == "__main__":
    main()