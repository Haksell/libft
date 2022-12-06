from ctypes import c_char_p, pointer, POINTER
from test_lstnew import ft_lstnew
from utils import libft, t_list

ft_lstadd_back = libft.ft_lstadd_back
ft_lstadd_back.argtypes = (
    POINTER(POINTER(t_list)),
    POINTER(t_list),
)
ft_lstadd_back.restype = None


def test_lstadd_back():
    lst = ft_lstnew(69)
    ft_lstadd_back(pointer(lst), ft_lstnew(42))
    ft_lstadd_back(pointer(lst), ft_lstnew(b"wololo"))
    assert lst.contents.content == 69
    assert lst.contents.next.contents.content == 42
    assert c_char_p(lst.contents.next.contents.next.contents.content).value == b"wololo"
    assert not lst.contents.next.contents.next.contents.next
