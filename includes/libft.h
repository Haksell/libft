/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   libft.h                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: axbrisse <axbrisse@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/11/07 11:27:39 by axbrisse          #+#    #+#             */
/*   Updated: 2022/12/09 10:15:34 by axbrisse         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef LIBFT_H
# define LIBFT_H

# include <stdbool.h>
# include <stdint.h>
# include <stddef.h>
# include <stdlib.h>
# include <unistd.h>

typedef struct s_list
{
	void			*content;
	struct s_list	*next;
}	t_list;

typedef struct s_dynamic_string {
	char	*content;
	size_t	length;
	size_t	capacity;
}	t_dynamic_string;

int					ft_atoi(const char *);
void				ft_bzero(void *, size_t );
void				*ft_calloc(size_t, size_t);
bool				ft_ds_extend(t_dynamic_string *s1, char *s2, size_t len2);
t_dynamic_string	ft_ds_new(char *s);
int					ft_isalpha(int);
int					ft_isalnum(int);
int					ft_isascii(int);
int					ft_isdigit(int);
int					ft_islower(int);
int					ft_isprint(int);
int					ft_isupper(int);
char				*ft_itoa(int);
void				ft_lstadd_back(t_list **, t_list *);
void				ft_lstadd_front(t_list **, t_list *);
void				ft_lstclear(t_list **, void (*)(void *));
void				ft_lstdelone(t_list *, void (*)(void*));
void				ft_lstiter(t_list *, void (*)(void *));
t_list				*ft_lstlast(t_list *);
t_list				*ft_lstmap(t_list *, void *(*)(void *), void (*)(void *));
t_list				*ft_lstnew(void *);
int					ft_lstsize(t_list *);
void				*ft_memchr(const void *, int, size_t);
int					ft_memcmp(const void *, const void *, size_t);
void				*ft_memcpy(void *, const void *, size_t);
void				*ft_memmove(void *, const void *, size_t);
void				*ft_memset(void *, int, size_t);
void				ft_putchar_fd(char, int);
void				ft_putendl_fd(char *, int);
void				ft_putnbr_fd(int, int);
void				ft_putstr_fd(char *, int);
char				**ft_split(char const *, char);
char				*ft_strchr(const char *, int);
char				*ft_strdup(const char *);
char				*ft_strjoin(char const *, char const *);
void				ft_striteri(char *, void (*)(unsigned int, char*));
char				*ft_strmapi(char const *, char (*)(unsigned int, char));
int					ft_strncmp(const char *, const char *, size_t);
char				*ft_strrchr(const char *, int);
size_t				ft_strlcat(char *, const char *, size_t);
size_t				ft_strlcpy(char *, const char *, size_t);
size_t				ft_strlen(const char *);
char				*ft_strnstr(const char *, const char *, size_t);
char				*ft_strtrim(char const *, char const *);
char				*ft_substr(char const *, unsigned int, size_t);
int					ft_tolower(int);
int					ft_toupper(int);

#endif
