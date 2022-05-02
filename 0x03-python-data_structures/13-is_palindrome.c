#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: a double pointer to the start of the list
 *
 * Return: 0 if it is not a palindrome, 1 if it is
 */
int is_palindrome(listint_t **head)
{
	int track = 0, idx = 0, length = 0;
	listint_t *ptr = *head;

	if (head == NULL || *head == NULL)
		return (0);

	while (ptr != NULL)
	{
		length++;
		ptr = ptr->next;
	}

	if (length < 2)
		return (0);

	idx = length / 2;
	while (idx > 0)
	{
		track += (*head)->n;
		*head = (*head)->next;
		idx--;
	}

	if (length % 2 != 0)
		*head = (*head)->next;

	while (*head != NULL)
	{
		track -= (*head)->n;
		*head = (*head)->next;
	}

	if (track == 0)
		return (1);
	else
		return (0);
}
