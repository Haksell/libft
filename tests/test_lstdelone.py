from ctypes import byref, c_void_p, CFUNCTYPE, POINTER
from test_lstadd_front import ft_lstadd_front
from test_lstnew import ft_lstnew
from utils import libft, t_list

func_type = CFUNCTYPE(None, c_void_p)

ft_lstdelone = libft.ft_lstdelone
ft_lstdelone.argtypes = (POINTER(t_list), func_type)
ft_lstdelone.restype = None


@func_type
def del_(_):
    return


def test_lstdelone():
    lst = POINTER(t_list)()
    ft_lstadd_front(byref(lst), ft_lstnew(27))
    ft_lstadd_front(byref(lst), ft_lstnew(42))
    ft_lstadd_front(byref(lst), ft_lstnew(69))
    ft_lstdelone(lst.contents.next.contents.next, del_)
    assert lst.contents.content == 69
    assert lst.contents.next.contents.content == 42
    assert lst.contents.next.contents.next.contents.content is None
