# A recursive function that gets input from a user and returns multiple values

def factorial(n):
    if n == 0 or n == 1:
        return n, 1
    return n, factorial(n - 1)[1] * n

num = int(input('Enter a number:'))
x, y = factorial(num)
print(f'{x}! is {y}')