"""
An algorithm that makes the sum of the even fibonacci numbers (lesser than 4,000,000) using recursion
"""

def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

sum = 0
for i in range(33):
    if fib(i)%2 == 0:
        sum = sum + fib(i)

print(sum)
