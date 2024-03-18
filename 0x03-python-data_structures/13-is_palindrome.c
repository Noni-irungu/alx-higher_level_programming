#include "lists.h"

/**
 * reverse_listint - A function that reverses
 * a linked list
 * @head: the pointer to the first node in the list
 *
 * Return: the pointer to the first node in the new list
 */
void reverse_listint(listint_t **head)
{
	listint_t *prvs, *nxt = NULL;
	listint_t *curnt = *head;

	while (curnt)
	{
		nxt = curnt->next;
		curnt->next = prvs;
		prvs = curnt;
		curnt = nxt;
	}

	*head = prvs;
}

/**
 * is_palindrome - A function that checks if
 * a linked list is a palindrome
 * @head: Adouble pointer to the linked list
 *
 * Return: 1 if it is, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *slw = *head, *fst = *head, *curnt_ptr = *head,
		  *rvs_ptr = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		fst = fst->next->next;
		if (!fst)
		{
			rvs_ptr = slw->next;
			break;
		}
		if (!fst->next)
		{
			rvs_ptr = slw->next->next;
			break;
		}
		slw = slw->next;
	}

	reverse_listint(&rvs_ptr);

	while (curnt_ptr && rvs_ptr)
	{
		if (curnt_ptr->n == rvs_ptr->n)
		{
			rvs_ptr = rvs_ptr->next;
			curnt_ptr = curnt_ptr->next;
		}
		else
			return (0);
	}

	if (!rvs_ptr)
		return (1);

	return (0);
}
