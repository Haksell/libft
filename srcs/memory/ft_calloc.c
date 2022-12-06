/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_calloc.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: axbrisse <axbrisse@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/11/08 20:32:10 by axbrisse          #+#    #+#             */
/*   Updated: 2022/11/17 04:05:00 by axbrisse         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_calloc(size_t nmemb, size_t size)
{
	void			*ptr;
	const size_t	bytes = nmemb * size;

	if (size > 0 && nmemb > SIZE_MAX / size)
		return (NULL);
	ptr = malloc(bytes);
	if (ptr != NULL)
		ft_bzero(ptr, bytes);
	return (ptr);
}
