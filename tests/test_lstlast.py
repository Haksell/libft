from ctypes import byref, c_char_p, POINTER
from test_lstadd_back import ft_lstadd_back
from test_lstnew import ft_lstnew
from utils import libft, t_list

ft_lstlast = libft.ft_lstlast
ft_lstlast.argtypes = (POINTER(t_list),)
ft_lstlast.restype = POINTER(t_list)


def test_lstlast():
    lst = POINTER(t_list)()
    assert not ft_lstlast(lst)
    ft_lstadd_back(byref(lst), ft_lstnew(69))
    assert ft_lstlast(lst).contents.content == 69
    ft_lstadd_back(byref(lst), ft_lstnew(b"wololo"))
    assert c_char_p(ft_lstlast(lst).contents.content).value == b"wololo"
