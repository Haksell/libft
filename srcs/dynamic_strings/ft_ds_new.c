/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_ds_new.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: axbrisse <axbrisse@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/12/09 10:00:38 by axbrisse          #+#    #+#             */
/*   Updated: 2022/12/18 19:04:56 by axbrisse         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

t_dynamic_string	ft_ds_new(char *s)
{
	const size_t		length = ft_strlen(s);
	t_dynamic_string	dynamic_string;

	if (s == NULL)
		dynamic_string.content = NULL;
	else
		dynamic_string.content = ft_substr(s, 0, length);
	dynamic_string.length = length;
	dynamic_string.capacity = length + 1;
	return (dynamic_string);
}
