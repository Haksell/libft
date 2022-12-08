from ctypes import addressof, cast, create_string_buffer, c_char_p, c_size_t
from utils import libft

ft_strdup = libft.ft_strdup
ft_strdup.argtypes = (c_char_p,)
ft_strdup.restype = c_size_t


def test_strdup():
    for word in (b"", b"lol", b"0123456789"):
        sb = create_string_buffer(word)
        dupped = ft_strdup(sb)
        arr = cast(dupped, c_char_p)
        assert addressof(sb) != dupped
        assert addressof(sb) != addressof(arr)
        assert word == arr.value
