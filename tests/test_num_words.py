from ctypes import c_char_p, c_size_t
from utils import libft

ft_num_words = libft.ft_num_words
ft_num_words.argtypes = (c_char_p, c_char_p)
ft_num_words.restype = c_size_t


def check(s, charset):
    mine = ft_num_words(
        bytes(s, "utf-8"),
        b"\t\n\v\r\f " if charset is None else bytes(charset, "utf-8"),
    )
    good = sum(map("".__ne__, s.split(charset)))
    assert mine == good, (s, charset, mine, good)


def test_basic():
    check("Je m'appelle Axel et j'aime le chocolat.", None)
    check("abababa", "b")


def test_around():
    check(" Je m'appelle Axel et j'aime le chocolat.", None)
    check("  Je m'appelle Axel et j'aime le chocolat.", None)
    check("Je m'appelle Axel et j'aime le chocolat. ", None)
    check("Je m'appelle Axel et j'aime le chocolat.  ", None)
    check(" Je m'appelle Axel et j'aime le chocolat. ", None)
    check("  Je m'appelle Axel et j'aime le chocolat.  ", None)


def test_multiple_in_a_row():
    check(" Je m'appelle    Axel     et j'aime le chocolat.", None)
    check("ana", "n")
    check("anna", "n")
    check("annna", "n")
    check("annnna", "n")
    check("annnnna", "n")


def test_no_split():
    check("Je m'appelle Axel et j'aime le chocolat.", "\0")
    check("Je m'appelle Axel et j'aime le chocolat.", "z")
