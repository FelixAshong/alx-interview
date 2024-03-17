#!/usr/bin/python3
"""
Contains isPrime and isWinner Functions
"""


def isPrime(n):
    """
    Returns prime numbers between 1 and n
    (sieve of Eratosthenes)
    """
    primeNums = []
    sieve = [True] * (n + 1)
    for num in range(2, n + 1):
        if sieve[num]:
            primeNums.append(num)
            for i in range(num, n + 1, num):
                sieve[i] = False
    return primeNums


def isWinner(x, nums):
    """Function to determine winner of Prime game"""
    if x is None or nums is None or x == 0 or nums == []:
        return None
    mariaCount = 0
    benCount = 0
    for n in range(x):
        primeNums = isPrime(nums[n])
        if len(primeNums) % 2 != 0:
            mariaCount += 1
        else:
            benCount += 1
    if mariaCount > benCount:
        return "Maria"
    elif benCount > mariaCount:
        return "Ben"
    else:
        return None
