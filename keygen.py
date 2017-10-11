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

def are_coprime(a, b):
    """Check whether two numbers are coprime.

    Args:
        a (int): First number.
        b (int): Second number.

    Returns:
        bool: True if they are coprime, False otherwise.

    """
    return gcd(a, b) == 1

def get_coprime_to(m):
    """Find a number smaller than m and coprime.

    Args:
        m (int): Input number.

    Returns:
        int: Smaller and coprime number to m. Note
             one always must exist, as 1 and m are coprime
             for any m > 1.

    """
    for e in xrange(m, 1, -1):
        if are_coprime(m, e):
            return e

def egcd(a, b):
    """Euclidean Algorithm for GCD.
    http://mathworld.wolfram.com/EuclideanAlgorithm.html

    Args:
        a (int): First number.
        b (int): Second number.

    Returns:
        tuple(int, int, int): The three numbers such that
        gcd(x, y) = ax + by (g, x, y)

    """
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - y * b / a, y)

def get_mul_inverse(a, n):
    """Get the multiplicative inverse of a modulo n
       within the range of 1 and n - 1. i.e., a number
       x such that ax = 1 mod n.

    Args:
        a (int): The number to find the multiplicative inverse.
        n (int): The number to work modulo

    Returns:
        tuple(int, int, int): The three numbers such that
        gcd(x, y) = ax + by (g, x, y)

    """
    g, x, _ = egcd(a, n)
    if g == 1:
        return x % n

PublicKey  = namedtuple('PublicKey', 'n, pub')
PrivateKey = namedtuple('PrivateKey', 'n, priv')

def keygen(size):
    """Public and private key generation. This is the bulk
       of RSA. Choose two random, large, prime numbers p and q.
       Set n = p * q, and set phi = (p - 1) * (q - 1).
       Set e to be a number prime to phi, and set d to be a
       multiplicative inverse of e mod phi. Then we have
       e * d = 1 mod phi  => phi * k + 1 = e * d for some k.
       Now as a public key give out the pair (n, e),
       and as a private key secure the pair (n, d).
       Whoever wants to communicate with you, gets their
       message M and computes C = M ^ e mod n, and sends you
       C. Now you, and only you can decipher C, as
       C ^ d = M ^ (ed) = M ^ (phi * k + 1) = M ^ (phi * k) * M
       = 1 * M = M mod n. The key is that due to Euler's Theorem,
       M ^ phi = 1 mod n.

    Args:
        size (int): Size of the key (the bigger the more secure, but slower)

    Returns:
        tuple(PublicKey, PrivateKey): Two named tuples each consisting
        of the pair (n, pub = e), and (n, priv = d).

    """
    assert 1 <= size <= 10, 'Size too big. Try a number between 1 and 10'
    min_size = 10 ** size
    max_size = 10 ** (size + 1)
    p = q = random_prime(min_size, max_size)
    while q == p:
        q = random_prime(min_size, max_size)
    phi = (p - 1) * (q - 1)
    n   = p * q
    e   = get_coprime_to(phi)
    d   = get_mul_inverse(e, phi)
    return PublicKey(n=n, pub=e), PrivateKey(n=n, priv=d)



