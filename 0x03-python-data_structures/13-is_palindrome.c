#include "lists.h"

/**
 * add_nodeint_start - adds a new node at the start of a listint_t list
 * @head: pointer to pointer of first node of listint_t list
 * @n: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */
listint_t *add_nodeint_start(listint_t **head, const int n)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = n;
	new->next = NULL;

	if (*head == NULL)
		*head = new;
	else
	{
		new->next = *head;
		*head = new;
	}

	return (new);
}

/**
 * length_list - Return the length of a linked list
 *
 * @head: pointer to pointer of first node of listint_t list
 *
 * Return: The length of listint_t list
 */
int length_list(listint_t **head)
{
	int length = 0;
	listint_t *current = *head;

	while (current != NULL)
	{
		current = current->next;
		length++;
	}

	return (length);
}

/**
 * new_linked_list - Copy a linked list in reverse
 *
 * @head: pointer to pointer of first node of listint_t list
 *
 * Return: A listint_t in reverse
 */
listint_t *new_linked_list(listint_t **head)
{
	listint_t *new = NULL;
	listint_t *current = *head;

	while (current != NULL)
	{
		add_nodeint_start(&new, current->n);
		current = current->next;
	}

	return (new);
}

/**
 * is_palindrome - Test a linked list if is a palindrome or not
 *
 * @head: pointer of pointer of first node of listint_t list
 *
 * Return: 0 if the linked list is not a palindrome,
 * 1 if the linked list is a palindrom
 */
int is_palindrome(listint_t **head)
{
	int length, end;
	listint_t *reverse, *current;

	if (head == NULL || *head == NULL)
		return (1);

	length = length_list(head);
	end = length;

	if (length == 1)
		return (1);

	reverse = new_linked_list(head);
	current = *head;

	while (end > length / 2)
	{
		if (current->n != reverse->n)
			return (0);
		current = current->next;
		reverse = reverse->next;
		end--;
	}

	return (1);
}
