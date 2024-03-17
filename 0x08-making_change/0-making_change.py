#!/usr/bin/python3
"""
Given a pile of coins of different values, determine the fewest
number of coins needed to meet a given amount total.
"""


def makeChange(coins, total):
    """
    Determines the fewest
    number of coins needed to meet a given amount total.
    """
    sum = 0
    if (total <= 0):
        return 0
    coins.sort(reverse=True)
    for i in coins:
        if (total < i):
            pass
        q, r = divmod(total, i)
        total = r
        sum += q
    if (total != 0):
        return -1
    return sum
