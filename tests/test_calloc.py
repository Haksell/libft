from ctypes import *  # TODO
from utils import libft

ft_calloc = libft.ft_calloc
ft_calloc.argtypes = (c_size_t, c_size_t)
ft_calloc.restype = c_void_p

SIZE_MAX = (1 << 64) - 1


def test_zero():
    assert ft_calloc(0, 4) is not None
    assert ft_calloc(4, 0) is not None


def test_overflow():
    assert ft_calloc(1 << 62, 4) is None
    assert ft_calloc(1 << 63, 2) is None
    assert ft_calloc(SIZE_MAX, 42) is None


def test_probably_too_big():
    assert ft_calloc(SIZE_MAX, 1) is None
    assert ft_calloc(1, SIZE_MAX) is None


def test_normal():
    size = 32
    arr = cast(ft_calloc(size, 4), POINTER(c_int))
    assert arr is not None
    assert all(arr[i] == 0 for i in range(size))
    # DANGER ZONE
    try:
        assert any(arr[i] != 0 for i in range(size, 2 * size))
        assert any(arr[-i] != 0 for i in range(1, size))
    except Exception as e:
        assert type(e) != AssertionError
