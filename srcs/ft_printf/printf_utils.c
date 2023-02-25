/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf2.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: axbrisse <axbrisse@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/02/24 22:28:37 by axbrisse          #+#    #+#             */
/*   Updated: 2023/02/24 22:28:56 by axbrisse         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static bool	write_and_free(t_dynamic_string *buffer, char *s)
{
	bool	result;

	if (s == NULL)
		return (false);
	result = ft_ds_extend(buffer, s, SIZE_MAX);
	free(s);
	return (result);
}

bool	write_nbr(t_dynamic_string *buffer, int n)
{
	return (write_and_free(buffer, ft_itoa(n)));
}

bool	write_nbr_base(t_dynamic_string *buffer, unsigned long n, char *base)
{
	return (write_and_free(buffer, ft_itoa_base(n, base)));
}

bool	write_ptr(t_dynamic_string *buffer, void *ptr)
{
	if (ptr == NULL)
		return (ft_ds_extend(buffer, "(nil)", SIZE_MAX));
	return (ft_ds_extend(buffer, "0x", SIZE_MAX)
		&& write_nbr_base(buffer, (unsigned long)ptr, HEXA_LOWER));
}

bool	write_str(t_dynamic_string *buffer, char *s)
{
	if (s == NULL)
		return (ft_ds_extend(buffer, "(null)", SIZE_MAX));
	return (ft_ds_extend(buffer, s, SIZE_MAX));
}
