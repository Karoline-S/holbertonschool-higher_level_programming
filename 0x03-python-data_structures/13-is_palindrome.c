#include <stdlib.h>
#include "lists.h"

/**
 * list_length - counts the nodes in a singly linked list
 * @head: a ptr to the start of the list
 * Return: number of nodes in the list
 */
int list_length(listint_t *head)
{
	int length = 0;

	while (head != NULL)
	{
		length++;
		head = head->next;
	}
	return (length);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: a double pointer to the start of the list
 *
 * Return: 0 if it is not a palindrome, 1 if it is
 */
int is_palindrome(listint_t **head)
{
	int track = 0, count = 0, length = 0;

	if (head == NULL || *head == NULL)
		return (1);

	length = list_length(*head);

	if (length == 1)
		return (1);

	count = length / 2;

	while (count > 0)
	{
		track += (*head)->n;
		*head = (*head)->next;
		count--;
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
