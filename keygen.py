from random import randrange
from fractions import gcd
from collections import namedtuple

def is_prime(n):
    """Check whether a given integer is prime. There are
       certainly faster algorithms for this (for example
       Miller-Rabin), but for the purpose of this
       exercise this method will do.

    Args:
        n (int): Number to check primality on.

    Returns:
        bool: True if n is prime, False otherwise.

    """
    if n % 2 == 0 or n == 1: 
        return False
    return all(n % i != 0 for i in xrange(3, int(n ** 0.5) + 1, 2))

def random_prime(min_size=10**8, max_size=10 ** 9):
    """Choose a random prime between two numbers.

    Args:
        min_size (int): Min size of prime.
        max_size (int): Max size of prime.

    Returns:
        int: The random prime between the selected range.

    """
    num = 0
    while not is_prime(num):
        num = randrange(min_size, max_size)
    return num
    