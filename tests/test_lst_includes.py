from ctypes import byref, POINTER, c_bool, c_void_p
from test_lstadd_front import ft_lstadd_front
from test_lstnew import ft_lstnew
from utils import libft, t_list

ft_lst_includes = libft.ft_lst_includes
ft_lst_includes.argtypes = (POINTER(t_list), c_void_p)
ft_lst_includes.restype = c_bool


def test_integers():
    lst = POINTER(t_list)()
    ft_lstadd_front(byref(lst), ft_lstnew(12))
    ft_lstadd_front(byref(lst), ft_lstnew(15))
    ft_lstadd_front(byref(lst), ft_lstnew(27))
    assert ft_lst_includes(lst, 12)
    assert ft_lst_includes(lst, 15)
    assert ft_lst_includes(lst, 27)
    assert not ft_lst_includes(lst, 0)
    assert not ft_lst_includes(lst, 13)
    assert not ft_lst_includes(lst, 21)
    assert not ft_lst_includes(lst, 42)
