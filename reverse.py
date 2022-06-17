"""


"""


def ecrypt_reverse(plaintext: str) -> str:
    """
    Return the encrypted message of plaintext with reverse encryption

    >>> ecrypt_reverse('encryption')
    'noitpyrcne'
    """
    ciphertext = ''
    for i in range(len(plaintext) - 1, -1, -1):
        ciphertext += str(plaintext[i])

    return ciphertext


def decrypt_reverse(ciphertext: str) -> str:
    """
    Return the decrypted message of ciphertext using the reverse encryption
    >>> ecrypt_reverse('noitpyrcne')
    'encryption'
    """
    plaintext = ''
    for i in range(len(ciphertext) - 1, -1, -1):
        ciphertext += str(ciphertext[i])
    return plaintext