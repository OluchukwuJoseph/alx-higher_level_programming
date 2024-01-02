#include "lists.h"

/**
 * check_cycle - Check if a linked list has a cycle.
 * @list: A pointer to the head of the linked list.
 *
 * Return: 1 if there is a cycle, 0 otherwise.
 */
int check_cycle(listint_t *list)
{
	listint_t *temp = list;

	while (temp != NULL)
	{
		if (temp->next == list)
			return (1);
		temp = temp->next;
	}
	return (0);
}
