from ctypes import CDLL, c_void_p, POINTER, Structure

class t_list(Structure):
    pass

t_list._fields_ = [("content", c_void_p), ("next", POINTER(t_list))]

libft = CDLL("./libft.so")