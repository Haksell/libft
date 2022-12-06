/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_atoi.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: axbrisse <axbrisse@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/11/08 20:06:21 by axbrisse          #+#    #+#             */
/*   Updated: 2022/11/09 13:08:37 by axbrisse         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_atoi(const char *nptr)
{
	unsigned int	absolute;
	int				i;
	int				sign;
	int				digit;

	i = 0;
	while (nptr[i] == ' ' || (nptr[i] >= 9 && nptr[i] <= 13))
		i++;
	sign = 1;
	if (nptr[i] == '-' || nptr[i] == '+')
	{
		if (nptr[i] == '-')
			sign = -sign;
		i++;
	}
	absolute = 0;
	while ('0' <= nptr[i] && nptr[i] <= '9')
	{
		digit = nptr[i] - '0';
		absolute = 10 * absolute + digit;
		i++;
	}
	return (absolute * sign);
}
