from ctypes import create_string_buffer, c_char_p, c_int
from utils import libft

ft_strncmp = libft.ft_strncmp
strncmp = libft.strncmp
ft_strncmp.argtypes = strncmp.argtypes = (c_char_p, c_char_p)
ft_strncmp.restype = strncmp.restype = c_int

def compare(s1, s2, n=1_000_000_000):
    s1 = create_string_buffer(bytes(s1, "utf-8"))
    s2 = create_string_buffer(bytes(s2, "utf-8"))
    assert ft_strncmp(s1, s2, n) == libft.strncmp(s1, s2, n)

def test_same():
    compare("a", "a", 1)
    compare("yolo", "yolo", 4)
    compare("bonjour", "bonsoir", 3)

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