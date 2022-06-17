"""


"""


def ecrypt_otp(k: str, plaintext: str) -> str:
    """
    Return the encrypted messafe of plaintext using the key k
    with the one-time pad cryptosystem

    >>> ecrypt_otp('avi', 'encryption')
    """

    ciphertext = ''
    for i in range(len(plaintext)):
        ciphertext = ciphertext + chr((ord(plaintext[i]) + ord(k[i])) % 128)

    return ciphertext


def decrypt_otp(k: str, ciphertext: str) -> str:
    """
    Return the decrypted message of ciphertext using the key k
    with the one-time pad cryptosystem
    """

    plaintext = ''
    for i in range(len(ciphertext)):
        plaintext = plaintext + chr((ord(ciphertext[i]) - ord(k[i])) % 128)

    return plaintext