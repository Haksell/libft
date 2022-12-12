from ctypes import c_char_p, c_int, c_size_t, c_ulong
from random import randint
from test_putchar_fd import ft_putchar_fd
from utils import libft
import os

ft_putbase_fd = libft.ft_putbase_fd
ft_putbase_fd.argtypes = (c_ulong, c_char_p, c_size_t, c_int)
ft_putbase_fd.restype = int

FILENAME = "tests/files/ft_putbase_fd"
ULONG_MAX = (1 << 64) - 1


def check(nums):
    for base, func in [
        (b"01", lambda n: bin(n)[2:]),
        (b"01234567", lambda n: oct(n)[2:]),
        (b"0123456789", str),
        (b"0123456789abcdef", lambda n: hex(n)[2:]),
    ]:
        with open(FILENAME, "w") as fp:
            fd = fp.fileno()
            for n in nums:
                ft_putbase_fd(n, base, len(base), fd)
                ft_putchar_fd(ord("\n"), fd)
        assert open(FILENAME).read() == "".join(f"{func(n)}\n" for n in nums)
    os.remove(FILENAME)


def test_limits():
    check([0, ULONG_MAX])


def test_small():
    check(list(range(1, 301)))


def test_random():
    check([randint(301, ULONG_MAX) for _ in range(100)])
