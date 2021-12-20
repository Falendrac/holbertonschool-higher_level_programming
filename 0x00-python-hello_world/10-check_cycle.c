#include "lists.h"

/**
 * check_cycle - Check if the linked list have a cycle
 *
 * @list: The linked list
 *
 * Return: 0 if there is no cycle, 1 otherwise
 */
int check_cycle(listint_t *list)
{
	int loop1 = 0, loop2 = 0;
	listint_t *current = list, *search = list;

	while (current != NULL)
	{
		current = current->next;
		loop1++;
		while (loop2 != loop1)
		{
			if (search == current && loop2 < loop1)
				return (1);
			search = search->next;
			loop2++;
		}
		search = list;
		loop2 = 0;
	}

	return (0);
}
