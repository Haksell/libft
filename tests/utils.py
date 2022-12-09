from ctypes import CDLL, c_char_p, c_size_t, c_void_p, POINTER, Structure

INT_MAX = (1 << 31) - 1
INT_MIN = ~INT_MAX


def sign(n):
    return 1 if n > 0 else -1 if n < 0 else 0


def same_sign(n1, n2):
    return sign(n1) == sign(n2)


class t_dynamic_string(Structure):
    _fields_ = [("content", c_char_p), ("length", c_size_t), ("capacity", c_size_t)]


class t_list(Structure):
    pass


t_list._fields_ = [("content", c_void_p), ("next", POINTER(t_list))]

libft = CDLL("./libft.so")
