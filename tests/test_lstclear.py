from ctypes import byref, c_void_p, CFUNCTYPE, pointer, POINTER
from test_lstadd_front import ft_lstadd_front
from test_lstnew import ft_lstnew
from utils import libft, t_list

func_type = CFUNCTYPE(None, c_void_p)

ft_lstclear = libft.ft_lstclear
ft_lstclear.argtypes = (POINTER(POINTER(t_list)), func_type)
ft_lstclear.restype = None


@func_type
def del_(_):
    return


def test_lstclear():
    node1 = ft_lstnew(69)
    node2 = ft_lstnew(42)
    node3 = ft_lstnew(27)
    lst = POINTER(t_list)()
    ft_lstadd_front(byref(lst), node3)
    ft_lstadd_front(byref(lst), node2)
    ft_lstadd_front(byref(lst), node1)
    ft_lstclear(pointer(lst.contents.next), del_)
    assert node1.contents.content == 69
    assert node2.contents.content != 42  # kind of shaky
    assert node3.contents.content != 27  # kind of shaky
