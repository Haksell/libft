/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: axbrisse <axbrisse@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/11/09 11:06:08 by axbrisse          #+#    #+#             */
/*   Updated: 2022/11/09 13:23:06 by axbrisse         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static size_t	get_num_words(char const *s, char c)
{
	bool	last_is_separator;
	size_t	res;
	size_t	i;

	last_is_separator = true;
	res = 0;
	i = 0;
	while (s[i] != '\0')
	{
		if (s[i] == c)
			last_is_separator = true;
		else
		{
			if (last_is_separator)
				res++;
			last_is_separator = false;
		}
		i++;
	}
	return (res);
}

static size_t	get_word_len(const char *s, char c)
{
	size_t	i;

	i = 0;
	while (s[i] && s[i] != c)
		i++;
	return (i);
}

static char	**free_words(char **words, size_t arr_idx)
{
	size_t	i;

	i = 0;
	while (i < arr_idx)
	{
		free(words[i]);
		i++;
	}
	free(words);
	return (NULL);
}

static char	*add_word(const char *s, size_t *i, char c)
{
	const size_t	word_len = get_word_len(s + *i, c);
	const size_t	bytes = word_len + 1;
	char			*dest;

	dest = malloc(sizeof(char) * bytes);
	if (dest != NULL)
		ft_strlcpy(dest, s + *i, bytes);
	*i = *i + word_len - 1;
	return (dest);
}

char	**ft_split(char const *s, char c)
{
	const size_t	num_words = get_num_words(s, c);
	char			**words;
	size_t			i;
	size_t			arr_idx;

	words = malloc(sizeof(char *) * (num_words + 1));
	if (words == NULL)
		return (NULL);
	i = 0;
	arr_idx = 0;
	while (s[i] != '\0')
	{
		if (s[i] != c)
		{
			words[arr_idx] = add_word(s, &i, c);
			if (words[arr_idx] == NULL)
				return (free_words(words, arr_idx));
			arr_idx++;
		}
		i++;
	}
	words[num_words] = NULL;
	return (words);
}
