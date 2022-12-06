from ctypes import c_char_p, pointer, POINTER
from test_lstnew import ft_lstnew
from utils import libft, t_list

ft_lstadd_front = libft.ft_lstadd_front
ft_lstadd_front.argtypes = (
    POINTER(POINTER(t_list)),
    POINTER(t_list),
)
ft_lstadd_front.restype = None


def test_lstadd_front():
    lst = ft_lstnew(69)
    ft_lstadd_front(pointer(lst), ft_lstnew(42))
    ft_lstadd_front(pointer(lst), ft_lstnew(b"wololo"))
    assert c_char_p(lst.contents.content).value == b"wololo"
    assert lst.contents.next.contents.content == 42
    assert lst.contents.next.contents.next.contents.content == 69
    assert not lst.contents.next.contents.next.contents.next
