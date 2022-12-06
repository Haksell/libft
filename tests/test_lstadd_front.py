from ctypes import *  # TODO
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
    ft_lstadd_front(byref(lst), ft_lstnew(42))
    ft_lstadd_front(byref(lst), ft_lstnew(b"wololo"))
    assert c_char_p(lst.contents.content).value == b"wololo"
    assert lst.contents.next.contents.content == 42
    assert lst.contents.next.contents.next.contents.content == 69
    assert not lst.contents.next.contents.next.contents.next


l1 = None
l2 = ft_lstnew(42)
for lst in (l1, l2):
    print(lst)
    try:
        print(pointer(lst))
    except Exception as e:
        print(e)
        pass
    try:
        print(byref(lst))
    except Exception as e:
        print(e)
        pass
    try:
        print(hex(addressof(lst)))
    except Exception as e:
        print(e)
        pass
    print("-" * 40)
