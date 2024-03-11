#include "lists.h"

/**
 * check_cycle - a function that checks if a list
 * contains a cycle.
 * @list: The list to check
 *
 * Return: (1) if there is cycle, (0) if none
 */
int check_cycle(listint_t *list)
{
	listint_t *turt = list;
	listint_t *rabb = list;

	if (!list)
		return (0);

	while (turt && rabb && rabb->next)
	{
		turt = turt->next;
		rabb = rabb->next->next;
		if (turt == rabb)
			return (1);
	}

	return (0);
}
