from ctypes import POINTER, c_char_p, c_int
from utils import libft

ft_strjoin_arr = libft.ft_strjoin_arr
ft_strjoin_arr.argtypes = (c_int, POINTER(c_char_p), c_char_p)
ft_strjoin_arr.restype = c_char_p


def check(arr_py, sep):
    expected = sep.join(arr_py)
    arr_c = (c_char_p * len(arr_py))()
    arr_c[:] = [s.encode() for s in arr_py]
    result = ft_strjoin_arr(len(arr_c), arr_c, sep.encode()).decode()
    assert expected == result


def test_strjoin_arr():
    for arr_py in [[], ["one"], ["one", "two"]]:
        for sep in ["", " ", ": "]:
            check(arr_py, sep)
