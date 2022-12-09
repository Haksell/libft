from ctypes import c_int
from random import randint
from test_putchar_fd import ft_putchar_fd
from utils import libft
import os

ft_putnbr_fd = libft.ft_putnbr_fd
ft_putnbr_fd.argtypes = (c_int, c_int)
ft_putnbr_fd.restype = None

FILENAME = "tests/files/ft_putnbr_fd"
INT_MAX = (1 << 31) - 1
INT_MIN = ~INT_MAX


def check(nums):
    with open(FILENAME, "w") as fp:
        fd = fp.fileno()
        for n in nums:
            ft_putnbr_fd(n, fd)
            ft_putchar_fd(ord("\n"), fd)
    assert open(FILENAME).read() == "".join(f"{n}\n" for n in nums)
    os.remove(FILENAME)


def test_limits():
    check([INT_MIN, INT_MAX])


def test_small():
    check(list(range(-200, 201)))


def test_random():
    check([randint(INT_MIN, INT_MAX) for _ in range(100)])
