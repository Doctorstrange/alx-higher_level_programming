#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 *print_dlistint - print all elements on the list
 *@h: head pointer
 *Return: number of nodes in list
 */

size_t print_dlistint(const dlistint_t *h)
{
	int number = 0;

	if (h == NULL)
		return (number);

	while (h->prev != NULL)
		h = h->prev;

	while (h != NULL)
	{
		printf("%d\n", h->n);
		number++;
		h = h->next;
	}

	return (number);
}
