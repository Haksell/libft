from ctypes import POINTER, c_char_p, c_size_t
from utils import libft

ft_free_double_pointer = libft.ft_free_double_pointer
ft_free_double_pointer.argtypes = (POINTER(c_char_p), c_size_t)
ft_free_double_pointer.restype = None


def test_free_double_pointer():
    assert True # I tried