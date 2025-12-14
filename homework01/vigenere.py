""" Модуль для шифрования и дешифрования текста с помощью шифра Виженера"""


def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""

    # Убираем не-буквенные символы из ключа
    clean_keyword = ''.join(char for char in keyword if char.isalpha())

    if not clean_keyword:
        return plaintext

    key_index = 0

    for char in plaintext:
        if char.isalpha():
            # Получаем текущий символ ключа
            key_char = clean_keyword[key_index % len(clean_keyword)]

            # Вычисляем сдвиг
            if key_char.isupper():
                shift = ord(key_char) - ord('A')
            else:
                shift = ord(key_char) - ord('a')

            # Применяем шифрование
            if char.isupper():
                base = ord('A')
                encrypted_char = chr((ord(char) - base + shift) % 26 + base)
            else:
                base = ord('a')
                encrypted_char = chr((ord(char) - base + shift) % 26 + base)

            ciphertext += encrypted_char
            key_index += 1
        else:
            # Не-буквенные символы (пробелы, цифры, знаки препинания) остаются без изменений
            ciphertext += char

    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    # PUT YOUR CODE HERE
    return plaintext
