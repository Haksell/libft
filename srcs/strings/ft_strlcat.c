/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcat.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: axbrisse <axbrisse@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/11/08 14:59:03 by axbrisse          #+#    #+#             */
/*   Updated: 2022/11/11 18:38:52 by axbrisse         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

size_t	ft_strlcat(char *dst, const char *src, size_t size)
{
	size_t	di;
	size_t	si;
	size_t	dst_len;
	size_t	src_len;
	size_t	concat_len;

	src_len = ft_strlen(src);
	di = 0;
	while (di < size && dst[di] != '\0')
		di++;
	dst_len = di;
	concat_len = dst_len + src_len;
	if (di == size)
		return (concat_len);
	si = 0;
	while (src[si] != '\0' && di < size - 1)
	{
		dst[di] = src[si];
		di++;
		si++;
	}
	dst[di] = '\0';
	return (concat_len);
}
