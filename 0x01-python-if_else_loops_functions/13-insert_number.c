#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - Insert in sorted linked list
 * @head: A pointer to linked list.
 * @number: The number to insert.
 *
 * Return: If the function fails - NULL.
 * Otherwise - a pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *place;

	place = malloc(sizeof(listint_t));
	if (place == NULL)
		return (NULL);
	place->n = number;

	if (node == NULL || node->n >= number)
	{
		place->next = node;
		*head = place;
		return (place);
	}

	while (node->next && node && node->next->n < number)
		node = node->next;

	place->next = node->next;
	node->next = place;

	return (place);
}
