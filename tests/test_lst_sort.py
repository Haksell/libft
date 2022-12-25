from ctypes import CFUNCTYPE, byref, POINTER, c_int, c_void_p
from random import randint, randrange
from test_lstnew import ft_lstnew
from test_lstadd_front import ft_lstadd_front
from utils import libft, lst_to_arr, t_list

ft_lst_sort = libft.ft_lst_sort
ft_lst_sort.argtypes = (POINTER(t_list),)
ft_lst_sort.restype = None

func_type = CFUNCTYPE(c_int, c_void_p, c_void_p)


@func_type
def cmp(n1, n2):
    return n1 - n2


def is_non_decreasing(a):
    return all(x <= y for x, y in zip(a, a[1:]))


def test_lst_sort():
    for _ in range(10):
        lst = POINTER(t_list)()
        for _ in range(randint(0, 20)):
            # TODO make it work with negative numbers
            ft_lstadd_front(byref(lst), ft_lstnew(randint(100, 200)))
        ft_lst_sort(lst, cmp)
        assert is_non_decreasing(lst_to_arr(lst))
