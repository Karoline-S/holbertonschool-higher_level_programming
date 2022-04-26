#include "lists.h"

/**
 * check_cycle - checks if a singly list has a cycle in it
 * @list: a pointer to the list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *fast = list;
	listint_t *slow = list;

	if (list == NULL || list->next == NULL)
		return (0);

	fast = fast->next;

	while (fast != NULL)
	{
		if (fast == slow)
			return (1);

		fast = fast->next;
		if (fast == NULL)
			return (0);

		fast = fast->next;
		slow = slow->next;
	}

	return (0);
}
