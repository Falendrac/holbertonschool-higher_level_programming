#include "lists.h"

int is_palindrome_recursive(listint_t **start, listint_t *end)
{
	int isp = 0;

	if (end == NULL)
		return (1);

	if (is_palindrome_recursive(start, end->next) == 0)
		return (0);

	if ((*start)->n == end->n)
		isp = 1;

	*start = (*start)->next;

	return (isp);
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
	listint_t *current;

	if (head == NULL || *head == NULL || (*head)->next == NULL)
		return (1);

	current = *head;

	return (is_palindrome_recursive(&current, current));
}
