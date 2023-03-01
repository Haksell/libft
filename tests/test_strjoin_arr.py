from ctypes import POINTER, c_char_p
from utils import libft

ft_strjoin_arr = libft.ft_strjoin_arr
ft_strjoin_arr.argtypes = (POINTER(c_char_p), c_char_p, c_char_p)
ft_strjoin_arr.restype = c_char_p


def check(arr_py, sep, end):
    expected = sep.join(arr_py) + end
    arr_c = (c_char_p * (len(arr_py) + 1))()
    arr_c[:] = [s.encode() for s in arr_py] + [None]
    result = ft_strjoin_arr(arr_c, sep.encode(), end.encode()).decode()
    assert expected == result


def test_strjoin_arr():
    for arr_py in [[], ["one"], ["one", "two"]]:
        for sep in ["", " ", ": "]:
            for end in ["", "\n"]:
                check(arr_py, sep, end)
