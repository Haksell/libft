from ctypes import byref, c_void_p, CFUNCTYPE, POINTER
from test_lstadd_front import ft_lstadd_front
from test_lstnew import ft_lstnew
from utils import libft, t_list

del_type = CFUNCTYPE(None, c_void_p)
func_type = CFUNCTYPE(c_void_p, c_void_p)

ft_lstmap = libft.ft_lstmap
ft_lstmap.argtypes = (POINTER(t_list), func_type, del_type)
ft_lstmap.restype = POINTER(t_list)


@del_type
def del_(_):
    return


@func_type
def func(n):
    return 2 * n


def test_lstmap():
    lst = POINTER(t_list)()
    ft_lstadd_front(byref(lst), ft_lstnew(27))
    ft_lstadd_front(byref(lst), ft_lstnew(42))
    ft_lstadd_front(byref(lst), ft_lstnew(69))
    mapped = ft_lstmap(lst, func, del_)
    assert mapped.contents.content == 138
    assert mapped.contents.next.contents.content == 84
    assert mapped.contents.next.contents.next.contents.content == 54
    assert not mapped.contents.next.contents.next.contents.next
