LIB = libft.a

PATH_SRCS += srcs/conversion
PATH_SRCS += srcs/ctype
PATH_SRCS += srcs/linked_lists
PATH_SRCS += srcs/memory
PATH_SRCS += srcs/output
PATH_SRCS += srcs/strings

FILES += ft_atoi
FILES += ft_bzero
FILES += ft_calloc
FILES += ft_isalnum
FILES += ft_isalpha
FILES += ft_isascii
FILES += ft_isdigit
FILES += ft_isprint
FILES += ft_itoa
FILES += ft_memchr
FILES += ft_memcmp
FILES += ft_memcpy
FILES += ft_memmove
FILES += ft_memset
FILES += ft_putchar_fd
FILES += ft_putendl_fd
FILES += ft_putnbr_fd
FILES += ft_putstr_fd
FILES += ft_split
FILES += ft_strchr
FILES += ft_strdup
FILES += ft_striteri
FILES += ft_strjoin
FILES += ft_strlcat
FILES += ft_strlcpy
FILES += ft_strlen
FILES += ft_strmapi
FILES += ft_strncmp
FILES += ft_strnstr
FILES += ft_strrchr
FILES += ft_strtrim
FILES += ft_substr
FILES += ft_tolower
FILES += ft_toupper
FILES += ft_lstadd_back
FILES += ft_lstadd_front
FILES += ft_lstclear
FILES += ft_lstdelone
FILES += ft_lstiter
FILES += ft_lstlast
FILES += ft_lstmap
FILES += ft_lstnew
FILES += ft_lstsize

SRCS = ${addsuffix .c, ${FILES}}

vpath %.c ${PATH_SRCS}

PATH_OBJS = objs
OBJS = ${patsubst %.c, ${PATH_OBJS}/%.o, ${SRCS}}

INCLUDES = includes

AR = ar rcs
CC = cc
CFLAGS = -Wall -Wextra -Werror

all: ${LIB}

${LIB}: ${OBJS}
	${AR} ${LIB} $^

${OBJS}: ${PATH_OBJS}/%.o: %.c ${HEADER}
	@mkdir -p ${PATH_OBJS}
	${CC} ${CFLAGS} -c $< -o $@ -I ${INCLUDES}

clean:
	rm -rf ${PATH_OBJS}

fclean: clean
	rm -f ${LIB}

re: fclean ${LIB}

test: re
	PYTHONDONTWRITEBYTECODE=1 pytest -p no:cacheprovider tests

.PHONY: all clean fclean re
