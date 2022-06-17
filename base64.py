"""


"""
import csv


def encrypt_base64(plaintext: str) -> str:
    """
    Return the encrypted message of plaintext using the key k
    with the one-time pad cryptosystem

    >>> encrypt_base64('avi')
    'YXZp'
    """
    binary_value = to_binary(plaintext)

    # Converting the Binary value into 24-bits
    count = 0
    while len(binary_value) % 24 != 0:
        binary_value += '00000000'
        count += 1

    # Grouping into 6 characters
    bit_lst = [binary_value[i:i + 6] for i in range(0, len(binary_value), 6)]

    base64_val = []
    for val in bit_lst:
        rec_val = int(val[5]) * (2**0) + int(val[4]) * (2**1) + int(val[3]) * (2**2) \
              + int(val[2]) * (2**3) + int(val[1]) * (2**4) + int(val[0]) * (2**5)

        base64_val += [rec_val]

    if count != 0:
        new_count = 0
        for i in range(len(base64_val) - 1,  0, -1):
            if count != new_count:
                base64_val[i] = -1
                new_count += 1

    # Converting base64_val into cipher_text using Encoding table
    cipher_text = ''
    for val in base64_val:
        cipher_text += load_base64_table('base64_encodingtable.csv', val)
    return cipher_text


def load_base64_table(encoding_file: str, base64_value: int) -> str:
    """
    Reads CSV File to return the Base64 value's corresponding character
    """
    with open(encoding_file) as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            if str(base64_value) == row[0]:
                return row[1]


def to_binary(plaintext: str) -> str:
    """
    Returns the binary stream of the plain-text
    >>> to_binary('avi')
    '011000010111011001101001'
    """
    byte_array = plaintext.encode()
    binary_int = int.from_bytes(byte_array, "big")
    binary_string = bin(binary_int)

    return binary_string[:1] + binary_string[2:]

# def decrypt_otp(k: str, ciphertext: str) -> str:
#     """
#     Return the decrypted message of ciphertext using the key k
#     with the one-time pad cryptosystem
#     """
