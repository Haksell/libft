from ctypes import create_string_buffer, c_char_p, c_int
from utils import libft

ft_strchr = libft.ft_strchr
strchr = libft.strchr
ft_strchr.argtypes = strchr.argtypes = (c_char_p, c_int)
ft_strchr.restype = strchr.restype = c_char_p

def compare(s, c):
    s = create_string_buffer(bytes(s, "utf-8"))
    c = ord(c)
    assert ft_strchr(s, c) == libft.strchr(s, c)

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