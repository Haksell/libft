import ctypes
from utils import libft, t_list

ft_lstnew = libft.ft_lstnew
ft_lstnew.argtypes = (ctypes.c_void_p,)
ft_lstnew.restype = ctypes.POINTER(t_list)


def test_int():
    lst = ft_lstnew(42)
    assert lst.contents.content == 42
    assert not lst.contents.next


def test_string():
    lst = ft_lstnew(b"42")
    assert ctypes.c_char_p(lst.contents.content).value == b"42"
    assert not lst.contents.next
