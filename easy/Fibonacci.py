num = int(input("Enter with the size of the fibonacci sequence that you want to generate: "))

def fib(n):
    if (n >= 3):
        return fib(n - 1) + fib(n - 2)
    else:
        return 1

for i in range(num):
    print(fib(i + 1))
