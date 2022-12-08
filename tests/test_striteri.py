from ctypes import CFUNCTYPE, c_char, c_char_p, c_uint, c_void_p, create_string_buffer
from utils import libft

func_type = CFUNCTYPE(None, c_uint, c_void_p)

ft_striteri = libft.ft_striteri
ft_striteri.argtypes = (c_char_p, func_type)
ft_striteri.restype = None


@func_type
def starify(_, c):
    c_char.from_address(c).value = 42


@func_type
def capitalize(i, c):
    memfield = c_char.from_address(c)
    memfield.value = memfield.value.upper() if i == 0 else memfield.value.lower()


def test_starify():
    sb = create_string_buffer(b"axel")
    ft_striteri(sb, starify)
    assert sb.value == b"****"


def test_capitalize():
    sb = create_string_buffer(b"Comment SA VA???!!")
    ft_striteri(sb, capitalize)
    assert sb.value == b"Comment sa va???!!"
