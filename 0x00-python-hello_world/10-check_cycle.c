#include "lists.h"

/**
 * check_cycle - check the code
 * @list: linked list to check
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
	listint_t *current = list;
	listint_t *after = list;

	if (!list)
		return (0);
	while (current && after && after->next)
	{
		current = current->next;
		after = after->next->next;
		if (current == after)
			return (1);
	}
	return (0);
}
