import os

CHECK_LEAKS = False
VALGRIND = "valgrind --leak-check=full --show-leak-kinds=all --track-origins=yes -q"
BUFFER_SIZES = [None, 1, 2, 3, 42, 1024]
CC = "cc -Wall -Wextra -Werror -g3 -I./includes"
FILES = "tests/gnl_files"
OUTPUT = "tests/files/output.txt"
SRCS = " ".join(
    [
        "srcs/get_next_line/get_next_line.c",
        "srcs/strings/ft_strlen.c",
        "srcs/strings/ft_strdup.c",
        "srcs/strings/ft_strjoin.c",
        "srcs/strings/ft_strlcpy.c",
    ]
)
ONE_FILE = "tests/gnl_mains/gnl_one_file"
INTERLEAVED = "tests/gnl_mains/gnl_interleaved"


def compile(test_name, buffer_size):
    define = "" if buffer_size is None else f"-D BUFFER_SIZE={buffer_size}"
    compilation = f"{CC} {define} {test_name}.c {SRCS} -o {test_name}"
    os.system(compilation)


def execute(test_name, args):
    execution = f"{VALGRIND if CHECK_LEAKS else ''} {test_name} {args} 1> {OUTPUT}"
    os.system(execution)


def check_one_file(iterations):
    filenames = os.listdir(FILES)
    for buffer_size in BUFFER_SIZES:
        compile(ONE_FILE, buffer_size)
        for filename in filenames:
            path = os.path.join(FILES, filename)
            execute(ONE_FILE, f"{path} {iterations}")
            output_lines = open(OUTPUT).read()
            path_lines = "".join(f"[{line}]" for line in open(path)) * iterations
            assert output_lines == path_lines, (
                buffer_size,
                path,
                output_lines,
                path_lines,
            )
            os.remove(OUTPUT)
    os.remove(ONE_FILE)


def test_once():
    check_one_file(1)


def test_twice():
    check_one_file(2)


def gnl_interleaved(filenames):
    files = [open(filename) for filename in filenames]
    while files:
        for file in files.copy():
            line = file.readline()
            if line:
                yield line
            else:
                files.remove(file)


def test_interleaved():
    filenames = [os.path.join(FILES, filename) for filename in os.listdir(FILES)]
    for buffer_size in BUFFER_SIZES:
        compile(INTERLEAVED, buffer_size)
        execute(INTERLEAVED, " ".join(filenames))
        output_lines = open(OUTPUT).read()
        path_lines = "".join(f"[{line}]" for line in gnl_interleaved(filenames))
        assert output_lines == path_lines, buffer_size
        os.remove(OUTPUT)
    os.remove(INTERLEAVED)
