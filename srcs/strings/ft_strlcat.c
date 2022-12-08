/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcat.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: axbrisse <axbrisse@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/11/08 14:59:03 by axbrisse          #+#    #+#             */
/*   Updated: 2022/12/08 10:50:29 by axbrisse         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

size_t	ft_strlcat(char *dst, const char *src, size_t size)
{
	size_t	i;

	src_len = ft_strlen(src);
	i = 0;
	while (i < size && dst[i] != '\0')
		i++;
	return (i + ft_strlcpy(dst + i, src, size - i));
}
