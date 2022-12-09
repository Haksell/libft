/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: axbrisse <axbrisse@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/12/09 10:55:49 by axbrisse          #+#    #+#             */
/*   Updated: 2022/12/09 11:59:23 by axbrisse         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static t_gnl_info	*init_gnl_info(void)
{
	t_gnl_info	*gnl_info;
	size_t		fd;

	gnl_info = malloc(sizeof(t_gnl_info));
	if (gnl_info == NULL)
		return (NULL);
	fd = 0;
	while (fd < FILE_DESCRIPTORS)
	{
		gnl_info->states[fd] = READING;
		gnl_info->strings[fd] = ft_ds_new("");
		fd++;
	}
	return (gnl_info);
}

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

static char	*strcut(t_dynamic_string *line, size_t middle)
{
	const char		*left = subnstr(line->content, 0, middle);
	const size_t	right_length = ft_strlen(line->content) - middle;
	const char		*right = subnstr(line->content, middle, right_length);

	free(line->content);
	if (left == NULL || right == NULL)
	{
		free((char *)left);
		free((char *)right);
		return (NULL);
	}
	*line = ft_ds_new((char *)right);
	free((char *)right);
	if (line->content == NULL)
	{
		free((char *)left);
		return (NULL);
	}
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
	static t_gnl_info		*gnl_info = NULL;
	size_t					nl_index;
	char					*return_value;

	if (gnl_info == NULL)
		gnl_info = init_gnl_info();
	if (fd < 0 || fd >= FILE_DESCRIPTORS || gnl_info == NULL
		|| gnl_info->states[fd] == FINISHED
		|| !keep_reading(fd, gnl_info->strings + fd, gnl_info->states + fd))
		return (NULL);
	nl_index = find_newline(gnl_info->strings[fd].content, SIZE_MAX);
	if (gnl_info->states[fd] == LAST_LINE && (nl_index == SIZE_MAX
			|| gnl_info->strings[fd].content[nl_index + 1] == '\0'))
	{
		gnl_info->states[fd] = FINISHED;
		return (gnl_info->strings[fd].content);
	}
	return_value = strcut(gnl_info->strings + fd, nl_index + 1);
	if (return_value == NULL)
		gnl_info->states[fd] = FINISHED;
	return (return_value);
}
