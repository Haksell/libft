from ctypes import c_char_p, c_int
from itertools import count, takewhile
import os
from utils import libft

get_next_line = libft.get_next_line
get_next_line.argtypes = (c_int,)
get_next_line.restype = c_char_p

DIRECTORY = "tests/files/get_next_line"

FILES = [open(os.path.join(DIRECTORY, filename)) for filename in os.listdir(DIRECTORY)]
first_test_done = False


def handle_file_closing():
    print(globals())
    global first_test_done
    if first_test_done:
        for file in FILES:
            file.close()
    else:
        first_test_done = True
        for file in FILES:
            file.seek(0)


def test_one_file():
    FILES = [
        open(os.path.join(DIRECTORY, filename)) for filename in os.listdir(DIRECTORY)
    ]
    for file in FILES:
        goal = [bytes(line, "utf-8") for line in file]
        file.seek(0)
        mine = list(
            takewhile(
                lambda line: line is not None,
                (get_next_line(file.fileno()) for _ in count()),
            )
        )
        assert mine == goal
    handle_file_closing()


def test_multiple_files():
    goal = []
    while True:
        lines = [file.readline() for file in FILES]
        lines = [bytes(line, "utf-8") if line else None for line in lines]
        if not any(lines):
            break
        goal.extend(lines)
    for file in FILES:
        file.seek(0)
    mine = []
    while True:
        lines = [get_next_line(file.fileno()) for file in FILES]
        if not any(lines):
            break
        mine.extend(lines)
    assert mine == goal
    handle_file_closing()
