import ctypes
from main import libft

ft_toupper = libft.ft_toupper
toupper = libft.toupper
ft_toupper.argtypes = toupper.argtypes = (ctypes.c_int,)
ft_toupper.restypes = ft_toupper.restypes = ctypes.c_int

def test_toupper():
    for i in range(256):
        assert ft_toupper(i) == toupper(i)

