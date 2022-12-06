from ctypes import addressof, POINTER
from test_lstnew import ft_lstnew
from utils import libft, t_list

ft_lstadd_front = libft.ft_lstadd_front
ft_lstadd_front.argtypes = (
    POINTER(POINTER(t_list)),
    POINTER(t_list),
)
ft_lstadd_front.restype = None


def test_lstadd_front():
    lst = None
    ft_lstadd_front(addressof(lst), ft_lstnew(42))
    assert lst.contents.content == 42
    assert not lst.contents.next
