from ctypes import byref, c_void_p, CFUNCTYPE, POINTER
from test_lstadd_front import ft_lstadd_front
from test_lstnew import ft_lstnew
from utils import libft, t_list

func_type = CFUNCTYPE(None, c_void_p)

ft_lstiter = libft.ft_lstiter
ft_lstiter.argtypes = (POINTER(t_list), func_type)
ft_lstiter.restype = None

sum_ = 0


@func_type
def func(n):
    global sum_
    sum_ += n


def test_lstiter():
    lst = POINTER(t_list)()
    ft_lstadd_front(byref(lst), ft_lstnew(27))
    ft_lstadd_front(byref(lst), ft_lstnew(42))
    ft_lstadd_front(byref(lst), ft_lstnew(69))
    ft_lstiter(lst, func)
    assert sum_ == 138
