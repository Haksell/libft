/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: axbrisse <axbrisse@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/12/12 08:51:07 by axbrisse          #+#    #+#             */
/*   Updated: 2022/12/12 09:07:53 by axbrisse         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static int	ft_putptr_nil(void *ptr)
{
	if (ptr == NULL)
		return (ft_putstr_fd("(nil)", STDOUT_FILENO));
	return (
		ft_putstr_fd("0x", STDOUT_FILENO)
		+ ft_putbase_fd((unsigned long)ptr, HEXA_LOWER, 16, STDOUT_FILENO)
	);
}

static int	ft_putstr_null(char *s)
{
	if (s == NULL)
		return (ft_putstr_fd("(null)", STDOUT_FILENO));
	return (ft_putstr_fd(s, STDOUT_FILENO));
}

static int	convert(char format_char, va_list ap)
{
	if (format_char == '%')
		return (ft_putchar_fd('%', STDOUT_FILENO));
	else if (format_char == 'c')
		return (ft_putchar_fd(va_arg(ap, int), STDOUT_FILENO));
	else if (format_char == 's')
		return (ft_putstr_null(va_arg(ap, char *)));
	else if (format_char == 'p')
		return (ft_putptr_nil(va_arg(ap, void *)));
	else if (format_char == 'd' || format_char == 'i')
		return (ft_putnbr_fd(va_arg(ap, int), STDOUT_FILENO));
	else if (format_char == 'u')
		return (ft_putbase_fd(va_arg(ap, unsigned int), DECIMAL, 10, STDOUT_FILENO));
	else if (format_char == 'x')
		return (ft_putbase_fd(va_arg(ap, unsigned int), HEXA_LOWER, 16, STDOUT_FILENO));
	else if (format_char == 'X')
		return (ft_putbase_fd(va_arg(ap, unsigned int), HEXA_UPPER, 16, STDOUT_FILENO));
	return (0);
}

int	ft_printf(const char *format, ...)
{
	int		written;
	size_t	i;
	va_list	ap;

	va_start(ap, format);
	written = 0;
	i = 0;
	while (format[i] != '\0')
	{
		if (format[i] == '%')
		{
			i++;
			written += convert(format[i], ap);
		}
		else
			written += ft_putchar_fd(format[i], STDOUT_FILENO);
		i++;
	}
	va_end(ap);
	return (written);
}