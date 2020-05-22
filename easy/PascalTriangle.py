"""
This will generate Pascal's triangle.
"""

#Define a factorial using recursion
def f(n):
    if n == 0:
        return 1
    else:
        return n*f(n - 1)

rows = int(input('Enter with the amount of rows that you want to generate: '))
row = ""
for i in range(rows):
    for j in range(i + 1):
        num = f(i)/(f(j)*f(i - j))
        row += str(num) + " "
    print(row)
    row = ""
