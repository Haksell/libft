/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   gnl_one_file.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: axbrisse <axbrisse@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/01/22 05:27:15 by axbrisse          #+#    #+#             */
/*   Updated: 2023/04/03 19:26:35 by axbrisse         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../../libft.h"
#include <fcntl.h>
#include <stdio.h>
#include <sys/stat.h>
#include <sys/types.h>

int	main(int argc, char **argv)
{
	char	*filename;
	int		iterations;
	int		fd;
	char	*line;
	int		i;

	(void)argc;
	filename = argv[1];
	iterations = atoi(argv[2]);
	i = 0;
	while (i++ < iterations)
	{
		fd = open(filename, O_RDONLY);
		line = get_next_line(fd);
		while (line != NULL)
		{
			printf("[%s]", line);
			free(line);
			line = get_next_line(fd);
		}
		close(fd);
	}
	return (0);
}
