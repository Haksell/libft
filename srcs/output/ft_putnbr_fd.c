/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putnbr_fd.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: axbrisse <axbrisse@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/11/09 14:46:50 by axbrisse          #+#    #+#             */
/*   Updated: 2022/11/11 23:13:26 by axbrisse         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static void	write_digit(int digit, int fd)
{	
	ft_putchar_fd(digit + '0', fd);
}

static void	ft_putnbr_positive(int n, int fd)
{
	int	tens;
	int	units;

	tens = n / 10;
	units = n % 10;
	if (tens > 0)
		ft_putnbr_positive(tens, fd);
	write_digit(units, fd);
}

void	ft_putnbr_fd(int n, int fd)
{
	if (n == -2147483648)
		ft_putstr_fd("-2147483648", fd);
	else if (n < 0)
	{
		write(fd, "-", 1);
		ft_putnbr_positive(-n, fd);
	}
	else
		ft_putnbr_positive(n, fd);
}
