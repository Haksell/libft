from ctypes import c_char_p, POINTER
from itertools import groupby, takewhile
from utils import libft

ft_split_set = libft.ft_split_set
ft_split_set.argtypes = (c_char_p, c_char_p)
ft_split_set.restype = POINTER(c_char_p)


def ft_split_set_py(s, charset):
    return ["".join(v) for k, v in groupby(s, key=charset.__contains__) if not k]


def check(s, charset):
    assert list(
        takewhile(
            lambda w: w is not None,
            ft_split_set(bytes(s, "utf-8"), bytes(charset, "utf-8")),
        )
    ) == [bytes(w, "utf-8") for w in ft_split_set_py(s, charset) if w != ""]


def test_basic():
    check("Je m'appelle Axel et j'aime le chocolat.", " \t\n\v\f\r")
    check("abababa", "b")


def test_around():
    check(" Je m'appelle Axel et j'aime le chocolat.", " \t\n\v\f\r")
    check("  Je m'appelle Axel et j'aime le chocolat.", " \t\n\v\f\r")
    check("Je m'appelle Axel et j'aime le chocolat. ", " \t\n\v\f\r")
    check("Je m'appelle Axel et j'aime le chocolat.  ", " \t\n\v\f\r")
    check(" Je m'appelle Axel et j'aime le chocolat. ", " \t\n\v\f\r")
    check("  Je m'appelle Axel et j'aime le chocolat.  ", " \t\n\v\f\r")


def test_multiple_in_a_row():
    check(" Je m'appelle    Axel     et j'aime le chocolat.", " \t\n\v\f\r")
    check("ana", "n")
    check("anna", "n")
    check("annna", "n")
    check("annnna", "n")
    check("annnnna", "n")


def test_no_split():
    check("Je m'appelle Axel et j'aime le chocolat.", "\0")
    check("Je m'appelle Axel et j'aime le chocolat.", "z")
