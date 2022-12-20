/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_num_words.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: axbrisse <axbrisse@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/12/21 00:23:34 by axbrisse          #+#    #+#             */
/*   Updated: 2022/12/21 00:23:41 by axbrisse         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

size_t	ft_num_words(char const *s, char c)
{
	bool	last_is_separator;
	size_t	res;
	size_t	i;

	last_is_separator = true;
	res = 0;
	i = 0;
	while (s[i] != '\0')
	{
		if (s[i] == c)
			last_is_separator = true;
		else
		{
			if (last_is_separator)
				res++;
			last_is_separator = false;
		}
		i++;
	}
	return (res);
}