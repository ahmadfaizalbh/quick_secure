import base64
from itertools import cycle


def _shuffle(code):
    return "".join(i + j for i, j in zip(code[::2], code[1::2][::-1] + "=")).strip("=")


def _build_char_right(num):
    num %= 1112064
    if num > 55295:
        num += 2048
    return chr(num)


def _build_bin_left(char, pos):
    num = ord(char)
    if num > 55295:
        if num < 57344:
            raise UnicodeError(
                f"'utf-8' codec can't encode character '{char}' "
                f"in position {pos}: surrogates not allowed")
        num -= 2048
    return num


def encrypt(message, password):
    length = len(message)
    key_codes = cycle(map(ord, password))
    ens = "".join(_build_char_right((_build_bin_left(s, i) + next(key_codes) + length - i))
                  for i, s in enumerate(message))
    code = base64.urlsafe_b64encode(ens.encode()).decode().strip("=")
    return _shuffle(code)


def decrypt(message, password):
    string = _shuffle(message)
    padding = 4 - (len(string) % 4)
    if padding != 4:
        string += "=" * padding
    key_codes = cycle(map(ord, password))
    message = base64.urlsafe_b64decode(message).decode()
    length = len(message)
    return "".join(_build_char_right((_build_bin_left(s, i) + i - next(key_codes) - length))
                   for i, s in enumerate(message))
