from ctypes import create_string_buffer, c_char_p, c_int
from utils import libft

ft_strrchr = libft.ft_strrchr
strrchr = libft.strrchr
ft_strrchr.argtypes = strrchr.argtypes = (c_char_p, c_int)
ft_strrchr.restype = strrchr.restype = c_char_p

def compare(s, c):
    s = create_string_buffer(bytes(s, "utf-8"))
    c = ord(c)
    assert ft_strrchr(s, c) == libft.strrchr(s, c)

def test_first():
    for s, c in [("yolo", 'y'), ("wesh", 'w'), ("ooooo", 'o')]:
        compare(s, c)

def test_in():
    for s, c in [("yolo", 'o'), ("wesh", 's'), ("oopoo", 'p')]:
        compare(s, c)

def test_last():
    for s, c in [("yolop", 'p'), ("wesh", 's'), ("oooops", 's')]:
        compare(s, c)

def test_out():
    for s, c in [("", 'o'), ("wesh", 'o'), ("oooooooooo", 'p')]:
        compare(s, c)

def test_null_character():
    for s in ["", "0", "yolo", "yolo\0wesh"]:
        compare(s, '\0')