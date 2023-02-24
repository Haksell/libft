/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: axbrisse <axbrisse@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/12/12 08:51:07 by axbrisse          #+#    #+#             */
/*   Updated: 2023/02/24 21:37:54 by axbrisse         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static int	ft_putptr_nil(t_dynamic_string *buffer, void *ptr)
{
	if (ptr == NULL)
		return (ft_ds_extend(buffer, "(nil)", SIZE_MAX));
	return (ft_ds_extend(buffer, "0x", SIZE_MAX)
		&& ft_putbase_fd((unsigned long)ptr, HEXA_LOWER, 16, 1));
}

static int	ft_putstr_null(t_dynamic_string *buffer, char *s)
{
	if (s == NULL)
		return (ft_ds_extend(buffer, "(null)", SIZE_MAX));
	return (ft_ds_extend(buffer, s, SIZE_MAX));
}

static bool	convert(t_dynamic_string *buffer, char format_char, va_list ap)
{
	if (format_char == '%')
		return (ft_ds_append(buffer, '%'));
	else if (format_char == 'c')
		return (ft_ds_append(buffer, va_arg(ap, int)));
	else if (format_char == 's')
		return (ft_putstr_null(va_arg(ap, char *)));
	else if (format_char == 'p')
		return (ft_putptr_nil(va_arg(ap, void *)));
	else if (format_char == 'd' || format_char == 'i')
		return (ft_putnbr_fd(va_arg(ap, int), 1));
	else if (format_char == 'u')
		return (ft_putbase_fd(va_arg(ap, unsigned int), DECIMAL, 10, 1));
	else if (format_char == 'x')
		return (ft_putbase_fd(va_arg(ap, unsigned int), HEXA_LOWER, 16, 1));
	else if (format_char == 'X')
		return (ft_putbase_fd(va_arg(ap, unsigned int), HEXA_UPPER, 16, 1));
	return (0);
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
	success = 0;
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
