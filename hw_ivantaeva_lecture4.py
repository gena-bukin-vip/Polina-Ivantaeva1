def sieve_of_eratosthenes():
    
    try:
        n = int(input("Введите целое число N (больше 1): "))
        if n <= 1:
            print("N должно быть больше 1.")
            return

        primes = [True] * (n + 1)
        primes[0] = primes[1] = False

        for i in range(2, int(n**0.5) + 1):
            if primes[i]:
                for j in range(i*i, n + 1, i):
                    primes[j] = False

        print("Простые числа от 2 до", n, ":")
        for i in range(2, n + 1):
            if primes[i]:
                print(i)

    except ValueError:
        print("Некорректный ввод. Введите целое число.")

sieve_of_eratosthenes()