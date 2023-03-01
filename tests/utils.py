# TODO test ft_clean, ft_free, ft_free_double_pointer

from ctypes import CDLL, c_char_p, c_int, c_size_t, c_void_p, POINTER, Structure

INT_MAX = (1 << 31) - 1
INT_MIN = ~INT_MAX


def sign(n):
    return (n > 0) - (n < 0)


def same_sign(n1, n2):
    return sign(n1) == sign(n2)


class t_dynamic_string(Structure):
    _fields_ = [("content", c_char_p), ("length", c_int), ("capacity", c_int)]


class t_list(Structure):
    pass


t_list._fields_ = [("content", c_void_p), ("next", POINTER(t_list))]


def lst_to_arr(lst):
    arr = []
    while lst:
        arr.append(lst.contents.content or 0)
        lst = lst.contents.next
    return arr


libft = CDLL("./libft.so")
