#include "lists.h"

/**
 * inser_node - a function that inserts a number into
 * a sorted singly-linked list.
 * @head: pointer to the firat node of the linked list.
 * @number: the number to insert.
 *
 * Return: NULL if function fails
 * or pointer to new node on success
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (node == NULL || node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	new->next = node->next;
	node->next = new;

	return (new);
}
