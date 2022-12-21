/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: axbrisse <axbrisse@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/12/09 10:55:49 by axbrisse          #+#    #+#             */
/*   Updated: 2022/12/21 05:24:12 by axbrisse         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static char	*subnstr(char *s, size_t start, size_t len)
{
	char	*dest;
	size_t	i;

	dest = malloc(len + 1);
	if (dest == NULL)
		return (NULL);
	i = 0;
	while (i < len)
	{
		dest[i] = s[i + start];
		i++;
	}
	dest[len] = '\0';
	return (dest);
}

static size_t	find_newline(char *s, size_t lim)
{
	size_t	i;

	i = 0;
	while (s[i] != '\0' && i < lim)
	{
		if (s[i] == '\n')
			return (i);
		i++;
	}
	return (SIZE_MAX);
}

static char	*strcut(char *content, char *buffer, size_t middle)
{
	const char		*left = subnstr(content, 0, middle);
	const size_t	right_length = ft_strlen(content) - middle;
	const char		*right = subnstr(content, middle, right_length);

	free(content);
	if (left == NULL || right == NULL)
	{
		free((char *)left);
		free((char *)right);
		return (NULL);
	}
	ft_strlcpy(buffer, right, SIZE_MAX);
	free((char *)right);
	return ((char *)left);
}

static bool	keep_reading(int fd, t_dynamic_string *line, bool *is_last_line)
{
	char	buffer[BUFFER_SIZE + 1];
	ssize_t	bytes_read;

	ft_bzero(buffer, BUFFER_SIZE + 1);
	bytes_read = BUFFER_SIZE;
	while (find_newline(buffer, bytes_read) == SIZE_MAX && !*is_last_line)
	{
		bytes_read = read(fd, buffer, BUFFER_SIZE);
		if (
			bytes_read == -1
			|| (bytes_read == 0 && line->length == 0)
			|| !ft_ds_extend(line, buffer, bytes_read)
		)
		{
			*is_last_line = false;
			free(line->content);
			return (false);
		}
		if (bytes_read < BUFFER_SIZE)
			*is_last_line = true;
	}
	return (true);
}

char	*get_next_line(int fd)
{
	static bool			is_last_line[FILE_DESCRIPTORS] = {false};
	static char			buffers[FILE_DESCRIPTORS][BUFFER_SIZE + 1] = {0};
	size_t				nl_index;
	char				*return_value;
	t_dynamic_string	line;

	if (fd < 0 || fd >= FILE_DESCRIPTORS)
		return (NULL);
	line = ft_ds_new(buffers[fd]);
	ft_bzero(buffers[fd], BUFFER_SIZE + 1);
	if (!keep_reading(fd, &line, is_last_line + fd))
		return (NULL);
	nl_index = find_newline(line.content, SIZE_MAX);
	if (is_last_line[fd]
		&& (nl_index == SIZE_MAX || line.content[nl_index + 1] == '\0'))
	{
		is_last_line[fd] = false;
		return (line.content);
	}
	return_value = strcut(line.content, buffers[fd], nl_index + 1);
	if (return_value == NULL)
		is_last_line[fd] = false;
	return (return_value);
}
