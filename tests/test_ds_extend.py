from ctypes import POINTER, byref, c_bool, c_char_p, c_size_t
from utils import libft, t_dynamic_string
from test_ds_new import ft_ds_new

ft_ds_extend = libft.ft_ds_extend
ft_ds_extend.argtypes = (POINTER(t_dynamic_string), c_char_p, c_size_t)
ft_ds_extend.restype = c_bool


def check_one(dynamic_string, content, len_start):
    expected_capacity = len_start + 1
    while expected_capacity <= len(content):
        expected_capacity <<= 1
    assert dynamic_string.content == content
    assert dynamic_string.length == len(content)
    assert dynamic_string.capacity == expected_capacity


def check_sequence(start, extensions):
    dynamic_string = ft_ds_new(start)
    content = start
    check_one(dynamic_string, content, len(start))
    for s in extensions:
        ft_ds_extend(byref(dynamic_string), s, len(s))
        content += s
        check_one(dynamic_string, content, len(start))


def test_ds_empty_empty():
    check_sequence(b"", [b"", b""])


def test_ds_not_empty_empty():
    check_sequence(b"yolo", [b""])


def test_first_push_is_costly():
    check_sequence(b"abcdefghijklmnopqrstuvwxyz", [b"!"])


def test_ds_one_by_one():
    check_sequence(b"", [b"a"] * 10)


def test_ds_two_by_two():
    check_sequence(b"", [b"ab"] * 10)


def test_double():
    check_sequence(b"a", [b"b", b"cd", b"efgh", b"ijklmnop"])


def test_triple():
    check_sequence(b"a", [b"bc", b"defghi", b"jklmnopqrstuvwxyz!"])


def test_triangle():
    check_sequence(b"", [b"a", b"bc", b"def", b"ghij", b"klmno", b"pqrstu", b"vwxyz!?"])
