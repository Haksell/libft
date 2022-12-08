from ctypes import c_char, c_char_p, POINTER
from itertools import takewhile
from utils import libft

ft_split = libft.ft_split
ft_split.argtypes = (c_char_p, c_char)
ft_split.restype = POINTER(c_char_p)


def check(s, c):
    assert list(
        takewhile(lambda w: w is not None, ft_split(bytes(s, "utf-8"), ord(c)))
    ) == [bytes(w, "utf-8") for w in s.split(c) if w != ""]


def test_basic():
    check("Je m'appelle Axel et j'aime le chocolat.", " ")
    check("abababa", "b")


def test_around():
    check(" Je m'appelle Axel et j'aime le chocolat.", " ")
    check("  Je m'appelle Axel et j'aime le chocolat.", " ")
    check("Je m'appelle Axel et j'aime le chocolat. ", " ")
    check("Je m'appelle Axel et j'aime le chocolat.  ", " ")
    check(" Je m'appelle Axel et j'aime le chocolat. ", " ")
    check("  Je m'appelle Axel et j'aime le chocolat.  ", " ")


def test_multiple_in_a_row():
    check(" Je m'appelle    Axel     et j'aime le chocolat.", " ")
    check("ana", "n")
    check("anna", "n")
    check("annna", "n")
    check("annnna", "n")
    check("annnnna", "n")


def test_no_split():
    check("Je m'appelle Axel et j'aime le chocolat.", "\0")
    check("Je m'appelle Axel et j'aime le chocolat.", "z")
