"""Модуль для шифрования и дешифрования шифром Цезаря.
Реализует классический шифр Цезаря с поддержкой разных сдвигов."""


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
    for ch in plaintext:
        if "A" <= ch <= "Z":
            # диапазон заглавных букв
            ciphertext += chr((ord(ch) - ord("A") + shift) % 26 + ord("A"))
        elif "a" <= ch <= "z":
            # диапазон строчных букв
            ciphertext += chr((ord(ch) - ord("a") + shift) % 26 + ord("a"))
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
    for ch in ciphertext:
        if "A" <= ch <= "Z":
            plaintext += chr((ord(ch) - ord("A") - shift) % 26 + ord("A"))
        elif "a" <= ch <= "z":
            plaintext += chr((ord(ch) - ord("a") - shift) % 26 + ord("a"))
        else:
            plaintext += ch
    return plaintext


if __name__ == "__main__":
    print("Тест шифрования 'PYTHON':", encrypt_caesar("PYTHON"))
    print("Тест дешифрования 'SBWKRQ':", decrypt_caesar("SBWKRQ"))
