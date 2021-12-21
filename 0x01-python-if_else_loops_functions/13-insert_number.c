#include "lists.h"

/**
 * insert_node - Insert a node by sort
 *
 * @head: The adress of the linked list
 * @number: The number we want to insert
 *
 * Return: NULL if head is null or the malloc failled
 * new otherwise
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *old, *current;

	if (head == NULL)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	current = *head;

	if (*head == NULL)
		*head = new;
	else
	{
		while (current != NULL && current->n < number)
		{
			old = current;
			current = current->next;
		}

		new->next = current;
		old->next = new;
	}

	return (new);
}
