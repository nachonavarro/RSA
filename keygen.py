from random import randrange

def is_prime(n):
    if n % 2 == 0 or n == 1: 
        return False
    return all(n % i != 0 for i in xrange(3, int(n**0.5) + 1, 2))

def random_prime(max_size=10 ** 9):
    num = max_size
    while not is_prime(num):
        num = randrange(max_size)
    return num
    