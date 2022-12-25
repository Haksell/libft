from ctypes import byref, POINTER, c_size_t, c_void_p
from test_lstadd_front import ft_lstadd_front
from test_lstnew import ft_lstnew
from utils import libft, t_list

ft_lst_get = libft.ft_lst_get
ft_lst_get.argtypes = (POINTER(t_list), c_size_t)
ft_lst_get.restype = c_void_p


def test_lst_get():
    lst = POINTER(t_list)()
    ft_lstadd_front(byref(lst), ft_lstnew(12))
    ft_lstadd_front(byref(lst), ft_lstnew(15))
    ft_lstadd_front(byref(lst), ft_lstnew(27))
    assert not ft_lst_get(lst, -1)
    assert ft_lst_get(lst, 0) == 27
    assert ft_lst_get(lst, 1) == 15
    assert ft_lst_get(lst, 2) == 12
    assert not ft_lst_get(lst, 3)
