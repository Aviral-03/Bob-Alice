"""


"""
import random
import math
from typing import Tuple


def gcd_extended(a: int, b: int) -> Tuple[int, int, int]:
    """
    Return the gcd of a and b, and integers p and q such that

    gcd(a, b) == p * a + b * q

    >>> gcd_extended(10, 3)
    (1, 1, -3)
    """
    x, y = a, b

    # Initialize px, qx, py and qy
    px, qx = 1, 0
    py, qy = 0, 1

    while y != 0:

        assert math.gcd(a, b) == math.gcd(x, y)
        assert x == px * a + qx * b
        assert y == py * a + qy * b

        q, r = divmod(x, y)

        x, y = y, r

        px, qx, py, qy = py, qy , px - q * py, qx - q * qy

    return (x, px, qx)


def modular_inverse(a: int, n: int) -> int:
    """
    Return the inverse of a modulo n, in the range 0 to n - 1 inclusive.

    >>> modular_inverse(10, 3) # 10 * 1 is equivalent to 1 modulo 3
    1
    """
    gcd, p, q = gcd_extended(a, n)

    assert gcd == 1

    if p > 0:
        return p
    else:
        return n + p


def rsa_generate_key(p: int, q: int) -> Tuple[Tuple[int, int, int], Tuple[int, int]]:
    """

    """
    n = p * q
    phi_n = (p - 1) * (q - 1)
    e = 2

    while math.gcd(e, phi_n) != 1:
        e += 1

    d = modular_inverse(e, phi_n)

    return ((p, q, d), (n, e))


def rsa_ecrypt(public_key: Tuple[int, int], plaintext: int) -> int:
    """
    Encrypt the given plaintext using the recipient's public key.
    """

    n = public_key[0]
    e = public_key[1]

    return plaintext ** e % n


def rsa_decrypt(private_key: Tuple[int, int, int], ciphertext: int) -> int:
    """
    Decrypt the given ciphertext using the recipient's private key.
    """
    
    p = private_key[0]
    q = private_key[1]
    d = private_key[2]

    return ciphertext ** d % (p * q)
