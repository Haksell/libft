/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   test.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: axbrisse <axbrisse@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/11/07 14:42:43 by axbrisse          #+#    #+#             */
/*   Updated: 2022/12/06 08:16:24 by axbrisse         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"
#include <assert.h>
#include <ctype.h>
#include <limits.h>
#include <stdbool.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <bsd/string.h>

// HELPERS

void print_arr_int(int *arr, size_t size) {
	printf("[");
	for (size_t i = 0; i < size; i++)
		printf(i == size - 1 ? "%d" : "%d, ", arr[i]);
	printf("]\n");
}

void print_arr_string(char **arr) {
	printf("[");
	size_t i = 0;
	while (arr[i]) {
		printf(arr[i+1] ? "\"%s\", " : "\"%s\"", arr[i]);
		i++;
	}
	printf("]\n");
}

void print_list(t_list *ll) {
	printf("-> ");
	while (ll)
	{
		printf("%lld -> ", (unsigned long long) (ll->content));
		ll = ll->next;
	}
	printf("NULL\n");
	return ;
}

bool same_sign(int n1, int n2) {
	if (n1 < 0) return (n2 < 0);
	else if (n1 > 0) return (n2 > 0);
	else return (n2 == 0);
}

bool equal_tab(char **a1, char **a2) {
	size_t i = 0;
	while (a1[i] && a2[i]) {
		if (strcmp(a1[i], a2[i]) != 0)
			return false;
		i++;
	}
	return !a1[i] && !a2[i];
}

bool lst_equal_tab(t_list *lst, long *tab, size_t size) {
	size_t i = 0;
	if (lst) printf("first %ld \n", (long)lst->content);
	else printf("lst is NULL\n");
	while (i < size && lst) {
		printf("lst=%ld arr=%ld\n", (long)lst->content, tab[i]);
		if ((long)lst->content != tab[i])
			return false;
		i++;
		lst = lst->next;
	}
	return !lst && i == size;
}

// UNIT TESTS

void test_isalpha() {
	assert(ft_isalpha('a'));
	assert(ft_isalpha('H'));
	assert(!ft_isalpha('4'));
}

void test_isdigit() {
	assert(ft_isdigit('4'));
	assert(!ft_isdigit('Z'));
}

void test_isalnum() {
	assert(ft_isalnum('a'));
	assert(ft_isalnum('A'));
	assert(ft_isalnum('9'));
	assert(!ft_isalnum('.'));
}

void test_isascii() {
	assert(!ft_isascii(-1));
	assert(ft_isascii(0));
	assert(ft_isascii(42));
	assert(ft_isascii(127));
	assert(!ft_isascii(-128));
}

void test_isprint() {
	assert(!ft_isprint('\n'));
	assert(ft_isprint(' '));
	assert(ft_isprint('H'));
	assert(ft_isprint('~'));
	assert(!ft_isprint(142));
}

void test_strlen() {
	assert(ft_strlen("") == 0);
	assert(ft_strlen("H") == 1);
	assert(ft_strlen("Ho") == 2);
	assert(ft_strlen("Hop") == 3);
	assert(ft_strlen("0123456789") == 10);
}

void test_memset() {
	char	s1[50];
	strcpy(s1, "This is not a test. Take cover.");
	char *s2 = ft_memset(s1, '*', 7);
	assert(strcmp(s1, "******* not a test. Take cover.") == 0);
	assert(strcmp(s2, "******* not a test. Take cover.") == 0);

	const size_t	size = 10;
	int				ic[size];
	for (size_t i = 0; i < size ; i++)
		ic[i] = 0;
	ft_memset(ic, '*', 9);
	assert(ic[0] == 707406378);
	assert(ic[1] == 707406378);
	assert(ic[2] == 42);
	assert(ic[3] == 0);
}

void test_bzero() {
	char	s1[50];
	strcpy(s1, "This is not a test. Take cover.");
	ft_bzero(s1 + 19, 7);
	assert(s1[30] == '.');
	assert(strcmp(s1, "This is not a test.") == 0);
	ft_bzero(s1, 1);
	assert(strcmp(s1, "") == 0);
	assert(s1[1] == 'h');

	const size_t	size = 10;
	int				ic[size];
	for (size_t i = 0; i < size ; i++)
		ic[i] = INT_MAX;
	ft_bzero(ic, 9);
	assert(ic[0] == 0);
	assert(ic[1] == 0);
	assert(ic[2] == INT_MAX - 255);
	assert(ic[3] == INT_MAX);
}

void test_memcpy() {
	char s1[50];
	char s2[50];
	strcpy(s1, "wolololololo");
	strcpy(s2, "zzzzzzzzzzzz");
	char *s3 = ft_memcpy(s2, s1, 5);
	assert(strcmp(s1, "wolololololo") == 0);
	assert(strcmp(s2, "wololzzzzzzz") == 0);
	assert(strcmp(s3, "wololzzzzzzz") == 0);

	assert(ft_memcpy(NULL, NULL, 5) == NULL);
}

void test_memmove() {
	char bigger1[] = "memmove can be very useful......";
	memmove(bigger1+20, bigger1+15, 11);
	char bigger2[] = "memmove can be very useful......";
	ft_memmove(bigger2+20, bigger2+15, 11);
	assert(strcmp(bigger1, bigger2) == 0);

	char smaller1[] = "memmove can be very useful......";
	memmove(smaller1+15, smaller1+20, 11);
	char smaller2[] = "memmove can be very useful......";
	ft_memmove(smaller2+15, smaller2+20, 11);
	assert(strcmp(smaller1, smaller2) == 0);

	char independent1[] = "memmove can be very useful......";
	memmove(independent1+5, independent1+20, 11);
	char independent2[] = "memmove can be very useful......";
	ft_memmove(independent2+5, independent2+20, 11);
	assert(strcmp(independent1, independent2) == 0);

	assert(ft_memmove(NULL, NULL, 5) == NULL);
}

void test_strlcpy() {
	char string[] = "Hello there, Venus";
	int sizes[4] = {19, 10, 1, 0};
	char *strings[4] = {"Hello there, Venus", "Hello the", "", ""};

	for (int i = 0; i < 4; i++) {
		char buffer[19];
		assert(ft_strlcpy(buffer, string, sizes[i]) == 18);
		assert(strncmp(buffer, strings[i], sizes[i]) == 0);
	}
}

void test_strlcat() {
	char s1[] = "abcdef";
    char s2[] = "ghijklmnopqrstuvwxyz";
	size_t sizes[8] = {0, 1, 5, 6, 7, 8, 26, 27};
	size_t returns[8] = {20, 21, 25, 26, 26, 26, 26, 26};
	char *strings[8] = {"abcdef", "abcdef", "abcdef", "abcdef", "abcdef", "abcdefg", "abcdefghijklmnopqrstuvwxy", "abcdefghijklmnopqrstuvwxyz"};

	for (int i = 0; i < 8; i++) {
    	char buffer[27];
		strcpy(buffer, s1);
		assert(ft_strlcat(buffer, s2, sizes[i]) == returns[i]);
		assert(strcmp(buffer, strings[i]) == 0);
	}
}

void test_toupper() {
	assert(ft_toupper('4') == '4');
	assert(ft_toupper('z') == 'Z');
	assert(ft_toupper('Z') == 'Z');
	assert(ft_toupper(324) == 324); // 'D' + 256
	assert(ft_toupper(356) == 356); // 'd' + 256
}

void test_tolower() {
	assert(ft_tolower('4') == '4');
	assert(ft_tolower('z') == 'z');
	assert(ft_tolower('Z') == 'z');
	assert(ft_tolower(324) == 324); // 'D' + 256
	assert(ft_tolower(356) == 356); // 'd' + 256
}

void test_strchr() {
	char	buffer[] = "abcdef";
	char	*ptr;
	
	ptr = ft_strchr(buffer, 'a');
	assert(ptr == buffer);
	ptr = ft_strchr(buffer, 'f');
	assert(ptr == buffer + 5);
	ptr = ft_strchr(buffer, 'f' + 512);
	assert(ptr == buffer + 5);
	ptr = ft_strchr(buffer, '\0');
	assert(ptr == buffer + 6);
	ptr = ft_strchr(buffer, 'z');
	assert(ptr == NULL);
}

void test_strrchr() {
	char	buffer[] = "abcdefabc";
	char	*ptr;
	
	ptr = ft_strrchr(buffer, 'a');
	assert(ptr == buffer + 6);
	ptr = ft_strrchr(buffer, 'f');
	assert(ptr == buffer + 5);
	ptr = ft_strrchr(buffer, 'f' + 512);
	assert(ptr == buffer + 5);
	ptr = ft_strrchr(buffer, '\0');
	assert(ptr == buffer + 9);
	ptr = ft_strrchr(buffer, 'z');
	assert(ptr == NULL);
}

void test_strncmp() {
	char *s1[5] = {"même", "même", "meme", "meme", "a"};
	char *s2[5] = {"meme", "meme", "meme", "mem", "b"};
	size_t sizes[5] = { 4, 1, 4, 4, 12 };
	for (size_t i = 0; i < 5; i++) {
		int my_res = ft_strncmp(s1[i], s2[i], sizes[i]);
		int true_res = strncmp(s1[i], s2[i], sizes[i]);
		assert(same_sign(my_res, true_res));
	}
	assert(ft_strncmp(NULL, NULL, 1) == 0);
}

void test_memchr() {
	int data[] = { 42, 512 };
	int tests[] = { 42, 2, 1, 0, 258 };

	for (size_t i = 0; i < sizeof(tests) / sizeof(int); i++) {
		unsigned char* ft_ptr = ft_memchr(data, tests[i], 8);
		unsigned char* ptr = memchr(data, tests[i], 8);
		assert(ptr == ft_ptr);
	}
}

void test_memcmp() {
	char *s1[5] = {"même", "même", "meme", "meme", "a"};
	char *s2[5] = {"meme", "meme", "meme", "mem", "b"};
	size_t sizes[5] = { 4, 1, 4, 4, 12 };
	for (size_t i = 0; i < 5; i++) {
		int my_res = ft_strncmp(s1[i], s2[i], sizes[i]);
		int true_res = strncmp(s1[i], s2[i], sizes[i]);
		assert(same_sign(my_res, true_res));
	}

	int a1[] = { 0, 0 };
	int a2[] = { 0, 0 };
	assert(same_sign(ft_memcmp(a1, a2, 8), memcmp(a1, a2, 8)));
	a1[1] = 256;
	assert(same_sign(ft_memcmp(a1, a2, 8), memcmp(a1, a2, 8)));
	a2[1] = 42;
	assert(same_sign(ft_memcmp(a1, a2, 8), memcmp(a1, a2, 8)));
	a1[1] = 42;
	assert(same_sign(ft_memcmp(a1, a2, 8), memcmp(a1, a2, 8)));
	a1[0] = 12345;
	assert(same_sign(ft_memcmp(a1, a2, 8), memcmp(a1, a2, 8)));
	a2[1] = 1234567;
	assert(same_sign(ft_memcmp(a1, a2, 8), memcmp(a1, a2, 8)));
}

void test_strnstr() {
	char *big = "abccde";
	char *little[] = { "a", "abc", "cc", "cde", "cde", "z", "", "", "abcde" };
	size_t len[] = { 6, 6, 6, 6, 5, 6, 6, 0, 6 };
	for (size_t i = 0; i < sizeof(len) / sizeof(size_t); i++) {
		char *ft_res = ft_strnstr(big, little[i], len[i]);
		char *res = strnstr(big, little[i], len[i]);
		assert(ft_res == res);
	}

	char haystack[30] = "aaabcabcd";
	char needle[10] = "aabc";
	char *empty = "";
	assert(ft_strnstr(haystack, needle, 0) == 0);
	assert(ft_strnstr(haystack, needle, -1) == haystack + 1);
	assert(ft_strnstr(haystack, "a", -1) == haystack);
	assert(ft_strnstr(haystack, "c", -1) == haystack + 4);
	assert(ft_strnstr(empty, "", -1) == empty);
	assert(ft_strnstr(empty, "", 0) == empty);
	assert(ft_strnstr(empty, "coucou", -1) == 0);
	assert(ft_strnstr(haystack, "aaabc", 5) == haystack);
	assert(ft_strnstr(empty, "12345", 5) == 0);
	assert(ft_strnstr(haystack, "abcd", 9) == haystack + 5);
	assert(ft_strnstr(haystack, "cd", 8) == NULL);
	assert(ft_strnstr(haystack, "a", 1) == haystack);
	assert(ft_strnstr("1", "a", 1) == NULL);
	assert(ft_strnstr("22", "b", 2) == NULL);
}

void test_atoi() {
	char *tests[] = { "42", " 000042" , "- 7", "--7", " -7", "+-12", "-+12", "-999-", "\t++42,", "\t42lol", "2147483647", "2147483648", "-2147483647", "-2147483648" };
	for (size_t i = 0; i < sizeof(tests) / sizeof(char *); i++) {
		int ft_res = ft_atoi(tests[i]);
		int res = atoi(tests[i]);
		assert(ft_res == res);
	}
}

void test_calloc() {
	int *ptr;
	int *ft_ptr;
	
	ptr = (int *)calloc(42, sizeof(int));
	ft_ptr = (int *)ft_calloc(42, sizeof(int));
	assert(ft_memcmp(ptr, ft_ptr, 42 * sizeof(int)) == 0);
	ptr = (int *)calloc(0, sizeof(int));
	ft_ptr = (int *)ft_calloc(0, sizeof(int));
	assert(ft_memcmp(ptr, ft_ptr, 0 * sizeof(int)) == 0);
	ft_ptr = (int *)ft_calloc(123456789123, sizeof(int));
	assert(ft_ptr == NULL);
	ft_ptr = (int *)ft_calloc(SIZE_MAX / 3, sizeof(int));
	assert(ft_ptr == NULL);
}

void test_strdup() {
	char *words[] = { "", "lol", "0123456789" };
	for (size_t i = 0; i < sizeof(words) / sizeof(char *); i++) {
		char *dupped = ft_strdup(words[i]);
		assert(words[i] != dupped);
		assert(strncmp(dupped, words[i], ft_strlen(words[i])) == 0);
	}
}

void test_substr() {
	char *s = "yolowesh";
	assert(strcmp(ft_substr(s, 4, 3), "wes") == 0);
	assert(strcmp(ft_substr(s, 4, 4), "wesh") == 0);
	assert(strcmp(ft_substr(s, 4, 5), "wesh") == 0);
	assert(strcmp(ft_substr(s, 12, 3), "") == 0);
	assert(strcmp(ft_substr(s, 0, 8), "yolowesh") == 0);
	assert(strcmp(ft_substr(s, 0, 20), "yolowesh") == 0);
	assert(strcmp(ft_substr(s, 0, 0), "") == 0);
	assert(strcmp(ft_substr(s, 7, 1), "h") == 0);
}

void test_strjoin() {
	assert(strcmp(ft_strjoin("yolo", "wesh"), "yolowesh") == 0);
	assert(strcmp(ft_strjoin("yolo", ""), "yolo") == 0);
	assert(strcmp(ft_strjoin("", "wesh"), "wesh") == 0);
}

void test_strtrim() {
	assert(strcmp(ft_strtrim("a", " \t\n"), "a") == 0);
	assert(strcmp(ft_strtrim("   a", " \t\n"), "a") == 0);
	assert(strcmp(ft_strtrim("   a\t", " \t\n"), "a") == 0);
	assert(strcmp(ft_strtrim("   a\tlol", " \t\n"), "a\tlol") == 0);
	assert(strcmp(ft_strtrim("", " \t\n"), "") == 0);
	assert(strcmp(ft_strtrim("aaaaaaaaaaaaa", "a"), "") == 0);
	assert(strcmp(ft_strtrim(" aaaa aaaaaaaaa", "a"), " aaaa ") == 0);
}

void test_split() {
	char **w1 = ft_split("Je m'appelle Axel et j'aime le chocolat.", ' ');
	char *e1[] = { "Je", "m'appelle", "Axel", "et" ,"j'aime", "le", "chocolat.", NULL };
	assert(equal_tab(w1, e1));

	char **w2 = ft_split("abc def   ", ' ');
	char *e2[] = { "abc", "def", NULL };
	assert(equal_tab(w2, e2));

	char **w3 = ft_split("             abc def g h  i j k l m n o p  ", ' ');
	char *e3[] = { "abc", "def", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", NULL };
	assert(equal_tab(w3, e3));

	char **w4 = ft_split("Je m'appelle Axel et j'aime le chocolat.", 'z');
	char *e4[] = { "Je m'appelle Axel et j'aime le chocolat.", NULL };
	assert(equal_tab(w4, e4));

	char **w5 = ft_split("Je m'appelle Axel et j'aime le chocolat.", '\0');
	char *e5[] = { "Je m'appelle Axel et j'aime le chocolat.", NULL };
	assert(equal_tab(w5, e5));

	char **w6 = ft_split("    ", ' ');
	char *e6[] = { NULL };
	assert(equal_tab(w6, e6));

	char **w7 = ft_split("", ' ');
	char *e7[] = { NULL };
	assert(equal_tab(w7, e7));
}

void test_itoa() {
	for (int i = -128; i <= 128; i++)
		assert(i == atoi(ft_itoa(i)));
	assert(strcmp(ft_itoa(-2147483648), "-2147483648") == 0);
	assert(strcmp(ft_itoa(-2147483647), "-2147483647") == 0);
	assert(strcmp(ft_itoa(-1), "-1") == 0);
	assert(strcmp(ft_itoa(-0), "0") == 0);
	assert(strcmp(ft_itoa(1), "1") == 0);
	assert(strcmp(ft_itoa(2147483647), "2147483647") == 0);
	assert(strcmp(ft_itoa(2147483648), "-2147483648") == 0);
}

char capitalize(unsigned int i, char c) {
	return i == 0 ? toupper(c) : tolower(c);
}

char loweri(unsigned int i, char c) {
	(void)i;
	return tolower(c);
}

char upperi(unsigned int i, char c) {
	(void)i;
	return toupper(c);
}

void test_strmapi() {
	assert(strcmp(ft_strmapi("wEsH lA FaMiLlE", capitalize), "Wesh la famille") == 0);
	assert(strcmp(ft_strmapi("wEsH lA FaMiLlE", loweri), "wesh la famille") == 0);
	assert(strcmp(ft_strmapi("wEsH lA FaMiLlE", upperi), "WESH LA FAMILLE") == 0);
	assert(strcmp(ft_strmapi("wEsH lA FaMiLlE", NULL), "wEsH lA FaMiLlE") == 0);
	assert(ft_strmapi(NULL, capitalize) == NULL);
}

void capitalize_ptr(unsigned int i, char *c) {
	*c = i == 0 ? toupper(*c) : tolower(*c);
}

void loweri_ptr(unsigned int i, char *c) {
	(void)i;
	*c = tolower(*c);
}

void upperi_ptr(unsigned int i, char *c) {
	(void)i;
	*c = toupper(*c);
}

void test_striteri() {
	char s[] = "wEsH lA FaMiLlE";
	ft_striteri(s, capitalize_ptr);
	assert(strcmp(s, "Wesh la famille") == 0);
	ft_striteri(s, loweri_ptr);
	assert(strcmp(s, "wesh la famille") == 0);
	ft_striteri(s, upperi_ptr);
	assert(strcmp(s, "WESH LA FAMILLE") == 0);
}

void test_putchar_fd() {
	printf("This should write 'ft_putchar_fd' | ");
	fflush(stdout);
	ft_putchar_fd('f', 1);
	ft_putchar_fd('t', 1);
	ft_putchar_fd('_', 1);
	ft_putchar_fd('p', 1);
	ft_putchar_fd('u', 1);
	ft_putchar_fd('t', 1);
	ft_putchar_fd('c', 1);
	ft_putchar_fd('h', 1);
	ft_putchar_fd('a', 1);
	ft_putchar_fd('r', 1);
	ft_putchar_fd('_', 1);
	ft_putchar_fd('f', 1);
	ft_putchar_fd('d', 1);
	ft_putchar_fd('\n', 1);
}

void test_putstr_fd() {
	printf("This should write 'ft_putstr_fd' | ");
	fflush(stdout);
	ft_putstr_fd("ft_", 1);
	ft_putstr_fd("putstr_", 1);
	ft_putstr_fd("fd", 1);
	ft_putstr_fd("\n", 1);
}

void test_putendl_fd() {
	printf("This should write 'ft_putendl_fd' | ");
	fflush(stdout);
	ft_putendl_fd("ft_putendl_fd", 1);
	printf("This should write nothing | ");
	fflush(stdout);
	ft_putendl_fd("", 1);
}

void test_putnbr_fd() {
	const int tests[] = { -2147483648, -2147483647, -1, 0, 1, 2147483647, 2147483648 };
	for (size_t i = 0; i < sizeof(tests) / sizeof(int); i++)
	{
		printf("This should write '%s' | ", ft_itoa(tests[i]));
		fflush(stdout);
		ft_putnbr_fd(tests[i], 1);
		ft_putchar_fd('\n', 1);
	}
	printf("This should write all integers in [-100, 100] | ");
	fflush(stdout);
	for (int i = -100; i <= 100; i++)
	{
		ft_putnbr_fd(i, 1);
		ft_putchar_fd(' ', 1);
	}
	ft_putchar_fd('\n', 1);
}

void test_lstnew() {
	void	*c1 = (void *)42;
	t_list	*l1 = ft_lstnew(c1);
	assert(l1->content == c1);
	assert(l1->next == NULL);

	void	*c2 = (void *)"lol";
	t_list	*l2 = ft_lstnew(c2);
	assert(l2->content == c2);
	assert(l2->next == NULL);
}

void test_lstadd_front() {
	t_list  *ll = NULL;
	long a1[] = { };
	assert(lst_equal_tab(ll, a1, 0));
	ft_lstadd_front(&ll, ft_lstnew((void *)27));
	long a2[] = { 27 };
	assert(lst_equal_tab(ll, a2, 1));
	ft_lstadd_front(&ll, ft_lstnew((void *)42));
	long a3[] = { 42, 27 };
	assert(lst_equal_tab(ll, a3, 2));
	ft_lstadd_front(&ll, ft_lstnew((void *)69));
	long a4[] = { 69, 42, 27 };
	assert(lst_equal_tab(ll, a4, 3));
	ft_lstadd_front(&ll, ft_lstnew((void *)111));
	long a5[] = { 111, 69, 42, 27 };
	assert(lst_equal_tab(ll, a5, 4));
}

void test_lstsize() {
	t_list  *ll = NULL;
	assert(ft_lstsize(ll) == 0);
	ft_lstadd_front(&ll, ft_lstnew((void *)27));
	assert(ft_lstsize(ll) == 1);
	ft_lstadd_front(&ll, ft_lstnew((void *)42));
	assert(ft_lstsize(ll) == 2);
	ft_lstadd_front(&ll, ft_lstnew((void *)69));
	assert(ft_lstsize(ll) == 3);
	ft_lstadd_front(&ll, ft_lstnew((void *)111));
	assert(ft_lstsize(ll) == 4);
}

void test_lstlast() {
	t_list  *ll = NULL;
	assert(ft_lstlast(ll) == NULL);
	ft_lstadd_front(&ll, ft_lstnew((void *)27));
	assert((long)ft_lstlast(ll)->content == 27);
	ft_lstadd_front(&ll, ft_lstnew((void *)42));
	assert((long)ft_lstlast(ll)->content == 27);
	ft_lstadd_front(&ll, ft_lstnew((void *)69));
	assert((long)ft_lstlast(ll)->content == 27);
	ft_lstadd_front(&ll, ft_lstnew((void *)111));
	assert((long)ft_lstlast(ll)->content == 27);
}

void test_lstadd_back() {
	t_list  *ll = NULL;
	long a1[] = { };
	assert(lst_equal_tab(ll, a1, 0));
	ft_lstadd_back(&ll, ft_lstnew((void *)27));
	long a2[] = { 27 };
	assert(lst_equal_tab(ll, a2, 1));
	ft_lstadd_back(&ll, ft_lstnew((void *)42));
	long a3[] = { 27, 42 };
	assert(lst_equal_tab(ll, a3, 2));
	ft_lstadd_back(&ll, ft_lstnew((void *)69));
	long a4[] = { 27, 42, 69 };
	assert(lst_equal_tab(ll, a4, 3));
	ft_lstadd_back(&ll, ft_lstnew((void *)111));
	long a5[] = { 27, 42, 69, 111 };
	assert(lst_equal_tab(ll, a5, 4));
}

void del(void *i) {
	(void)i;
	return ;
}

void test_lstdelone() {
	// pretty much useless
	t_list  *ll = NULL;
	ft_lstadd_front(&ll, ft_lstnew((void *)27));
	ft_lstadd_front(&ll, ft_lstnew((void *)42));
	ft_lstadd_front(&ll, ft_lstnew((void *)69));
	ft_lstadd_front(&ll, ft_lstnew((void *)111));
	ft_lstdelone(ll->next->next, del);
	assert((long)ll->content == 111);
	assert((long)ll->next->content == 69);
}

void test_lstclear() {
	t_list  *ll = NULL;
	ft_lstadd_front(&ll, ft_lstnew((void *)27));
	ft_lstadd_front(&ll, ft_lstnew((void *)42));
	ft_lstadd_front(&ll, ft_lstnew((void *)69));
	ft_lstadd_front(&ll, ft_lstnew((void *)111));
	long a1[] = { 111, 69, 42, 27 };
	assert(lst_equal_tab(ll, a1, 4));
	ft_lstclear(&ll->next->next, del);
	long a2[] = { 111, 69 };
	assert(lst_equal_tab(ll, a2, 2));
	ft_lstclear(&ll, del);
	long a3[] = { };
	assert(lst_equal_tab(ll, a3, 0));
}

void print_elem(void *content) {
	ft_putchar_fd('.', 1);
	ft_putnbr_fd((long)(content) * 2, 1);
}

void test_lstiter() {
	t_list  *ll = NULL;
	ft_lstadd_front(&ll, ft_lstnew((void *)27));
	ft_lstadd_front(&ll, ft_lstnew((void *)42));
	ft_lstadd_front(&ll, ft_lstnew((void *)69));
	ft_lstadd_front(&ll, ft_lstnew((void *)111));
	
	printf("This should write '.222.138.84.54.' | ");
	fflush(stdout);
	ft_lstiter(ll, print_elem);
	ft_putstr_fd(".\n", 1);
}

void *succ(void *content){
	return content + 1;
}

void test_lstmap() {
	t_list  *l1 = NULL;
	t_list  *l2 = ft_lstmap(l1, succ, del);
	assert(l2 == NULL);

	ft_lstadd_front(&l1, ft_lstnew((void *)27));
	ft_lstadd_front(&l1, ft_lstnew((void *)42));
	ft_lstadd_front(&l1, ft_lstnew((void *)69));
	ft_lstadd_front(&l1, ft_lstnew((void *)111));
	t_list  *l3 = ft_lstmap(l1, succ, del);
	long a3[] = { 112, 70, 43, 28 };
	assert(lst_equal_tab(l3, a3, 4));
}

int	main(void)
{
	printf("Let's start testing!\n");
	test_isalpha(); printf("isalpha: OK\n");
	test_isdigit(); printf("isdigit: OK\n");
	test_isalnum(); printf("isalnum: OK\n");
	test_isascii(); printf("isascii: OK\n");
	test_isprint(); printf("isprint: OK\n");
	test_strlen(); printf("strlen: OK\n");
	test_memset(); printf("memset: OK\n");
	test_bzero(); printf("bzero: OK\n");
	test_memcpy(); printf("memcpy: OK\n");
	test_memmove(); printf("memmove: OK\n");
	test_strlcpy(); printf("strlcpy: OK\n");
	test_strlcat(); printf("strlcat: OK\n");
	test_toupper(); printf("toupper: OK\n");
	test_tolower(); printf("tolower: OK\n");
	test_strchr(); printf("strchr: OK\n");
	test_strrchr(); printf("strrchr: OK\n");
	test_strncmp(); printf("strncmp: OK\n");
	test_memchr(); printf("memchr: OK\n");
	test_memcmp(); printf("memcmp: OK\n");
	test_strnstr(); printf("strnstr: OK\n");
	test_atoi(); printf("atoi: OK\n");
	test_calloc(); printf("calloc: OK\n");
	test_strdup(); printf("strdup: OK\n");
	test_substr(); printf("substr: OK\n");
	test_strjoin(); printf("strjoin: OK\n");
	test_strtrim(); printf("strtrim: OK\n");
	test_split(); printf("split: OK\n");
	test_itoa(); printf("itoa: OK\n");
	test_strmapi(); printf("strmapi: OK\n");
	test_striteri(); printf("striteri: OK\n");
	test_putchar_fd(); printf("putchar_fd: OK\n");
	test_putstr_fd(); printf("putstr_fd: OK\n");
	test_putendl_fd(); printf("putendl_fd: OK\n");
	test_putnbr_fd(); printf("putnbr_fd: OK\n");
	test_lstnew(); printf("lstnew: OK\n");
	test_lstadd_front(); printf("lstadd_front: OK\n");
	test_lstsize(); printf("lstsize: OK\n");
	test_lstlast(); printf("lstlast: OK\n");
	test_lstadd_back(); printf("lstadd_back: OK\n");
	test_lstdelone(); printf("lstdelone: OK\n");
	test_lstclear(); printf("lstclear: OK\n");
	test_lstiter(); printf("lstiter: OK\n");
	test_lstmap(); printf("lstmap: OK\n");
	printf("Good.\n");
}