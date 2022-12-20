from ctypes import c_char, c_char_p, c_size_t
from utils import libft

ft_num_words = libft.ft_num_words
ft_num_words.argtypes = (c_char_p, c_char)
ft_num_words.restype = c_size_t


def check(s, c):
    assert ft_num_words(bytes(s, "utf-8"), ord(c)) == sum(w != "" for w in s.split(c) if w != "")


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
