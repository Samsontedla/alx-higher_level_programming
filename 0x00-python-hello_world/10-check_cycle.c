#include "lists.h"
/**
 * check_cycle - Checks if a singly-linked list contains a cycle.
 * @list: A singly-linked list.
 * Return: If there is no cycle - 0.
 *         If there is a cycle - 1.
 */
int check_cycle(listint_t *list)
{
	listint_t *front;
	listint_t *back;

	if (list == NULL || list->next == NULL)
	{
		return (0);
	}

	back = list->next;
	front = list->next->next;

	while (back && front && front->next)
	{
		if (back == front)
			return (1);

		back = back->next;
		front = front->next->next;
	}
	return (0);
}
