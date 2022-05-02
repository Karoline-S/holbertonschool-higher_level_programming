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
 * compare_nodes - compares the int held in two different nodes
 * @head: a pointer to the start of the list
 * @length: the length of the list
 * Return: the difference between the two ints
 */
int compare_nodes(listint_t *head, int length)
{
	int node1, node2;

	node1 = head->n;

	while (length > 1)
	{
		head = head->next;
		length--;
	}

	node2 = head->n;

	return (node1 - node2);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: a double pointer to the start of the list
 *
 * Return: 0 if it is not a palindrome, 1 if it is
 */
int is_palindrome(listint_t **head)
{
	int check, halfway = 0, length = 0;

	if (head == NULL || *head == NULL)
		return (1);

	length = list_length(*head);

	if (length == 1)
		return (1);

	halfway = length / 2;

	while (halfway > 0)
	{
		check = compare_nodes(*head, length);

		if (check != 0)
			return (0);

		*head = (*head)->next;
		halfway--;
		length -= 2;
	}

	return (1);
}
