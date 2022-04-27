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
	listint_t *compare, *new;

	if (head == NULL)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL)
	{
		*head = new;
		return (new);
	}
	if ((*head)->n > new->n)
	{
		new->next = *head;
		*head = new;
		return (new);
	}

	compare = *head;

	while (compare->next != NULL)
	{
		if (compare->next->n > new->n)
		{
			new->next = compare->next;
			compare->next = new;
			return (new);
		}
		compare = compare->next;
	}

	compare->next = new;
	new->next = NULL;
	return (new);
}
