/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: axbrisse <axbrisse@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/12/12 08:51:07 by axbrisse          #+#    #+#             */
/*   Updated: 2023/02/24 22:32:39 by axbrisse         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static bool	convert(t_dynamic_string *buffer, char format_char, va_list ap)
{
	if (format_char == '%')
		return (ft_ds_append(buffer, '%'));
	else if (format_char == 'c')
		return (ft_ds_append(buffer, va_arg(ap, int)));
	else if (format_char == 's')
		return (write_str(buffer, va_arg(ap, char *)));
	else if (format_char == 'p')
		return (write_ptr(buffer, va_arg(ap, void *)));
	else if (format_char == 'd' || format_char == 'i')
		return (write_nbr(buffer, va_arg(ap, int)));
	else if (format_char == 'u')
		return (write_nbr_base(buffer, va_arg(ap, unsigned int), DECIMAL));
	else if (format_char == 'x')
		return (write_nbr_base(buffer, va_arg(ap, unsigned int), HEXA_LOWER));
	else if (format_char == 'X')
		return (write_nbr_base(buffer, va_arg(ap, unsigned int), HEXA_UPPER));
	return (false);
}

int	ft_printf(const char *format, ...)
{
	t_dynamic_string	buffer;
	bool				success;
	va_list				ap;
	size_t				i;

	buffer = ft_ds_new("");
	if (buffer.content == NULL)
		return (-1);
	va_start(ap, format);
	i = 0;
	while (format[i] != '\0')
	{
		if (format[i] == '%')
			success = convert(&buffer, format[++i], ap);
		else
			success = ft_ds_append(&buffer, format[i]);
		if (!success)
			return (va_end(ap), free(buffer.content), -1);
		i++;
	}
	va_end(ap);
	return (write(STDOUT_FILENO, buffer.content, ft_strlen(buffer.content)));
}
