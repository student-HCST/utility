# myutility.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact