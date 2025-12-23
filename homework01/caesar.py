a = 26  # количество букв в латинском алфавите


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.
    Args:
        plaintext: Исходный текст для шифрования
        shift: Величина сдвига (по умолчанию 3)
    Returns:
        Зашифрованный текст
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    ord_A = ord("A")
    ord_a = ord("a")
    for ch in plaintext:
        if "A" <= ch <= "Z":
            # диапазон заглавных букв
            ciphertext += chr((ord(ch) - ord_A + shift) % a + ord_A)
        elif "a" <= ch <= "z":
            # диапазон строчных букв
            ciphertext += chr((ord(ch) - ord_a + shift) % a + ord_a)
        else:
            # остальные символы не меняем
            ciphertext += ch
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.
     Args:
        ciphertext: Зашифрованный текст
        shift: Величина сдвига (по умолчанию 3)
    Returns:
        Расшифрованный текст
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    ord_A = ord("A")
    ord_a = ord("a")
    for ch in ciphertext:
        if "A" <= ch <= "Z":
            # диапазон заглавных букв
            plaintext += chr((ord(ch) - ord_A - shift) % a + ord_A)
        elif "a" <= ch <= "z":
            # диапазон строчных букв
            plaintext += chr((ord(ch) - ord_a - shift) % a + ord_a)
        else:
            # остальные символы не меняем
            plaintext += ch
    return plaintext


if __name__ == "__main__":
    print("Тест шифрования 'PYTHON':", encrypt_caesar("PYTHON"))
    print("Тест дешифрования 'SBWKRQ':", decrypt_caesar("SBWKRQ"))
