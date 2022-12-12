/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: axbrisse <axbrisse@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/12/09 10:55:49 by axbrisse          #+#    #+#             */
/*   Updated: 2022/12/12 08:31:12 by axbrisse         ###   ########.fr       */
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

static bool	keep_reading(int fd, t_dynamic_string *line, t_gnl_state *state)
{
	char	buffer[BUFFER_SIZE + 1];
	ssize_t	bytes_read;

	ft_bzero(buffer, BUFFER_SIZE + 1);
	bytes_read = BUFFER_SIZE;
	while (find_newline(buffer, bytes_read) == SIZE_MAX && *state == READING)
	{
		bytes_read = read(fd, buffer, BUFFER_SIZE);
		if (
			bytes_read == -1
			|| (bytes_read == 0 && line->length == 0)
			|| !ft_ds_extend(line, buffer, bytes_read)
		)
		{
			*state = FINISHED;
			free(line->content);
			return (false);
		}
		if (bytes_read < BUFFER_SIZE)
			*state = LAST_LINE;
	}
	return (true);
}

char	*get_next_line(int fd)
{
	static t_gnl_state	states[FILE_DESCRIPTORS] = {0};
	static char			buffers[FILE_DESCRIPTORS][BUFFER_SIZE + 1] = {0};
	size_t				nl_index;
	char				*return_value;
	t_dynamic_string	line;

	if (BUFFER_SIZE <= 0 || FILE_DESCRIPTORS <= 0
		|| fd < 0 || fd >= FILE_DESCRIPTORS
		|| states[fd] == FINISHED)
		return (NULL);
	line = ft_ds_new(buffers[fd]);
	ft_bzero(buffers[fd], BUFFER_SIZE + 1);
	if (!keep_reading(fd, &line, states + fd))
		return (NULL);
	nl_index = find_newline(line.content, SIZE_MAX);
	if (states[fd] == LAST_LINE
		&& (nl_index == SIZE_MAX || line.content[nl_index + 1] == '\0'))
	{
		states[fd] = FINISHED;
		return (line.content);
	}
	return_value = strcut(line.content, buffers[fd], nl_index + 1);
	if (return_value == NULL)
		states[fd] = FINISHED;
	return (return_value);
}
