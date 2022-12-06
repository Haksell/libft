from ctypes import byref, c_int, POINTER
from test_lstadd_front import ft_lstadd_front
from test_lstnew import ft_lstnew
from utils import libft, t_list

ft_lstsize = libft.ft_lstsize
ft_lstsize.argtypes = (POINTER(t_list),)
ft_lstsize.restype = c_int


def test_lstsize():
    lst = POINTER(t_list)()
    assert ft_lstsize(lst) == 0
    ft_lstadd_front(byref(lst), ft_lstnew(69))
    assert ft_lstsize(lst) == 1
    ft_lstadd_front(byref(lst), ft_lstnew(42))
    assert ft_lstsize(lst) == 2
    ft_lstadd_front(byref(lst), ft_lstnew(b"wololo"))
    assert ft_lstsize(lst) == 3
