from ctypes import c_char_p
from utils import libft, t_dynamic_string

ft_ds_new = libft.ft_ds_new
ft_ds_new.argtypes = (c_char_p,)
ft_ds_new.restype = t_dynamic_string


def test_ds_new_contentful():
    for b in [b"", b"y", b"he", b"oui", b"yolo"]:
        ds = ft_ds_new(b)
        assert ds.content == b
        assert ds.length == len(b)
        assert ds.capacity == len(b) + 1


def test_ds_new_null():
    ds = ft_ds_new(None)
    assert ds.content == None
    assert ds.length == -1
    assert ds.capacity == -1
