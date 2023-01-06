from ctypes import POINTER, byref, c_bool, c_char
from utils import libft, t_dynamic_string
from test_ds_new import ft_ds_new

ft_ds_append = libft.ft_ds_append
ft_ds_append.argtypes = (POINTER(t_dynamic_string), c_char)
ft_ds_append.restype = c_bool


def check_one(dynamic_string, content, capacity):
    assert dynamic_string.content == content
    assert dynamic_string.length == len(content)
    assert dynamic_string.capacity == capacity


def test_ds_append():
    dynamic_string = ft_ds_new(b"")
    content = b""
    capacity = 1
    check_one(dynamic_string, content, capacity)
    for c in "yolowesh":
        ft_ds_append(byref(dynamic_string), ord(c))
        content += bytes([ord(c)])
        if len(content) >= capacity:
            capacity <<= 1
        check_one(dynamic_string, content, capacity)
