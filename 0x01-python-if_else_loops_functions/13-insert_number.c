#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts node into a sorted singly linked list
 * @head: pointer to pointer to the start of the list
 * @number: the int to be inserted with the new node
 * Return: a pointer to the new node or NULL if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *compare, *previous, *new;

	if (head == NULL)
		return (NULL);

	new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if ((*head)->n > number || *head == NULL)
	{
		if (*head == NULL)
		{
			*head = new;
			return (new);
		}
		else
		{
			new->next = *head;
			*head = new;
			return (new);
		}
	}

	previous = *head;
	compare = (*head)->next;

	while (compare != NULL)
	{
		if (compare->n > new->n)
		{
			new->next = compare;
			previous->next = new;
			return (new);
		}
		else
		{
			compare = compare->next;
			previous = previous->next;
		}
	}

	previous->next = new;
	new->next = NULL;
	return (new);
}
