#include "lists.h"
#include <stddef.h>
#include <stdio.h>

listint_t *r_listint(listint_t **head);
int is_palindrome(listint_t **head);

/**
 * reverse_listint - Reverses a singly-linked
 * @head: pointer to starting node of the list to reverse.
 *
 * Return: pointer to the head of the reversed list.
 */
listint_t *r_listint(listint_t **head)
{
	listint_t *node = *head, *next, *prev = NULL;

	while (node)
	{
		next = node->next;
		node->next = prev;
		prev = node;
		node = next;
	}

	*head = prev;
	return (*head);
}

/**
 * is_palindrome - is singly linked list is a palindrome.
 * @head: pointer to  head of the linked list.
 *
 * Return: list is not a pal
 *         list is a pali
 */
int is_palindrome(listint_t **start)
{
	listint_t *temp, *reverse, *middle;
	size_t size = 0, i;

	if (*start == NULL || (*start)->next == NULL)
		return (1);

	temp = *start;
	while (temp)
	{
		size++;
		temp = temp->next;
	}

	temp = *start;
	for (i = 0; i < (size / 2) - 1; i++)
		temp = temp->next;

	if ((size % 2) == 0 && temp->n != temp->next->n)
		return (0);

	temp = temp->next->next;
	reverse = r_listint(&temp);
	middle = reverse;

	temp = *start;
	while (reverse)
	{
		if (temp->n != reverse->n)
			return (0);
		temp = temp->next;
		reverse = reverse->next;
	}
	r_listint(&middle);

	return (1);
}
