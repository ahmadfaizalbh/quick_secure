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


def encode(string, key):
    length = len(string)
    key_codes = cycle(map(ord, key))
    ens = "".join(_build_char_right((_build_bin_left(s, i) + next(key_codes) + length - i))
                  for i, s in enumerate(string))
    code = base64.urlsafe_b64encode(ens.encode()).decode().strip("=")
    return _shuffle(code)


def decode(decode_string, key):
    string = _shuffle(decode_string)
    padding = 4 - (len(string) % 4)
    if padding != 4:
        string += "=" * padding
    key_codes = cycle(map(ord, key))
    string = base64.urlsafe_b64decode(string).decode()
    length = len(string)
    return "".join(_build_char_right((_build_bin_left(s, i) + i - next(key_codes) - length))
                   for i, s in enumerate(string))
