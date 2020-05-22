"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""

Nums = []

num = 2**1000

numStr = str(num)

for i in range(len(numStr)):
    Nums.append(int(numStr[i]))

print(sum(Nums))
