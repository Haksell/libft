/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   gnl_interleaved.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: axbrisse <axbrisse@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/01/22 05:27:11 by axbrisse          #+#    #+#             */
/*   Updated: 2023/01/22 05:45:55 by axbrisse         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../../includes/libft.h"
#include <fcntl.h>
#include <stdio.h>
#include <sys/stat.h>
#include <sys/types.h>

static int	*init_fds(int argc, char **argv)
{
	int	i;
	int	*fds;

	i = 1;
	fds = malloc(sizeof(int) * (argc - 1));
	while (i < argc)
	{
		fds[i - 1] = open(argv[i], O_RDONLY);
		++i;
	}
	return (fds);
}

static void	clear_fd(int *fd)
{
	close(*fd);
	*fd = -1;
}

static bool	la_norm_est_pas_tres_sympa(char *line)
{
	printf("[%s]", line);
	free(line);
	return (true);
}

int	main(int argc, char **argv)
{
	char	*line;
	int		*fds;
	bool	any_unfinished;
	int		i;

	fds = init_fds(argc, argv);
	any_unfinished = true;
	while (any_unfinished)
	{
		any_unfinished = false;
		i = 0;
		while (i < argc - 1)
		{
			line = get_next_line(fds[i]);
			if (line == NULL)
				clear_fd(fds + i);
			else
				any_unfinished = la_norm_est_pas_tres_sympa(line);
			++i;
		}
	}
	free(fds);
	return (0);
}
