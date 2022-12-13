from ctypes import create_string_buffer, c_char_p, c_int
from utils import libft, same_sign

ft_strcmp = libft.ft_strcmp
strcmp = libft.strcmp
ft_strcmp.argtypes = strcmp.argtypes = (c_char_p, c_char_p)
ft_strcmp.restype = strcmp.restype = c_int


def compare(s1, s2):
    s1 = create_string_buffer(bytes(s1, "utf-8"))
    s2 = create_string_buffer(bytes(s2, "utf-8"))
    assert same_sign(ft_strcmp(s1, s2), libft.strcmp(s1, s2))


def test_same():
    compare("a", "a")
    compare("yolo", "yolo")
    compare("bonjour", "bonjour")


def test_empty():
    compare("", "")
    compare("", "oui")
    compare("non", "")


def test_start():
    compare("bonjour", "bon")
    compare("oui", "ouioui")
    compare("oooooooo", "ooooooooooooooooooo")


def test_random():
    compare("bonjour", "bonsoir")
    compare("jambon", "jamie")
    compare("oops", "ooops")
    compare("oui", "non")


def test_nonascii():
    compare("SOIRÉE", "SOIREE")
