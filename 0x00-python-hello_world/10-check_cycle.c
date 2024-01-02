#include "lists.h"

/**
 * check_cycle - Check if a linked list has a cycle.
 * @list: A pointer to the head of the linked list.
 *
 * Return: 1 if there is a cycle, 0 otherwise.
 */
int check_cycle(listint_t *list)
{
	listint_t *fast = list;
	listint_t *slow = fast;

	while (fast != NULL && fast->next != NULL)
	{
		/*Move the slow pointer by one step*/
		slow = slow->next;
		/*Move the fast pointer by two steps*/
		fast = fast->next->next;
		if (fast == slow)
			return (1);
	}
	return (0);
}
