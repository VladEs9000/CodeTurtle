import hashlib
import os
import random
from Crypto.Cipher import AES
from Crypto import Random


_salt = b'random'
_block_size = 16  # Размер блока
_IV456 = b'yo_esK1DOHg2x-3L'  # Вектор инициализации


def hash_password(pas: str) -> str:
    if isinstance(pas, str) is False:
        raise TypeError(r"Не совпадение значений")
    salty = 'random'
    salt_byte = _salt
    return hashlib.sha256(salt_byte + pas.encode()).hexdigest() + ':' + salty


def check_password(hashed_password: str, user_pass: str) -> bool:
    if isinstance(hashed_password, str) is False:
        raise TypeError(r"Формат хеш-пароля не подходит")
    if isinstance(user_pass, str) is False:
        raise TypeError(r"Формат пользовательского пароля не подходит")
    checked_password = hashed_password.split(':')
    password = checked_password[0]
    salt = checked_password[1]
    check_key = hashlib.sha256(salt.encode() + user_pass.encode()).hexdigest()
    return password == check_key


def master_key(password: str) -> bytes:
    if isinstance(password, str) is False:
        raise TypeError(r"Не совпадение значений")
    master = hashlib.pbkdf2_hmac('sha256', password.encode(), _salt, 100000)
    return master


def secret_key() -> bytes:
    key = Random.new().read(32)
    return key


def fill_random_bytes(text: bytes, length: int) -> bytes:
    while len(text) % length != 0:  # кратно 16 байт
        symbol = bytes()
        if len(text) > 0:
            pos = random.randint(0, len(text))
            symbol = text[pos: pos + 1]
        text += symbol
    return text


def encrypt(message: bytes, secret_key: bytes) -> bytes:
    if isinstance(message, bytes) is False:
        raise TypeError(r"Формат текста не подходит")
    if isinstance(secret_key, bytes) is False:
        raise TypeError(r"Формат ключа не подходит")
    len_block = len(message).to_bytes(length=_block_size, byteorder='big')
    message = len_block + message
    message_byte = fill_random_bytes(message, _block_size)
    obj = AES.new(secret_key, AES.MODE_CBC, _IV456)
    ciphertext = obj.encrypt(message_byte)
    return ciphertext


def decrypt(ciphertext: bytes, key: bytes) -> bytes:
    if isinstance(ciphertext, bytes) is False:
        raise TypeError(r"Неподходящий формат шифротекста")
    if isinstance(key, bytes) is False:
        raise TypeError(r"Неподходящий формат ключа")
    if len(ciphertext) % _block_size != 0:
        raise ValueError(r"Длина шифротекста не кратна блоку")
    obj = AES.new(key, AES.MODE_CBC, _IV456)
    text = obj.decrypt(ciphertext)
    size = int.from_bytes(text[:_block_size], byteorder='big')
    text = text[_block_size:size + _block_size]
    return text
