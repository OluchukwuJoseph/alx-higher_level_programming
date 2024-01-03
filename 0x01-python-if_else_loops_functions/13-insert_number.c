#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - Inserts a new node with a given value into a sorted list
 *
 * @head: A pointer to the head of the linked list
 * @n: The value to be inserted into the linked list
 *
 * Return: A pointer to the newly inserted node
 * or NULL if memory allocation fails.
 */
listint_t *insert_node(listint_t **head, int n)
{
	listint_t *new, *temp;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = n;
	new->next = NULL;
	if (*head == NULL)
	{
		*head = new;
		return (*head);
	}
	temp = *head;
	if (temp->n > new->n)
	{
		new->next = temp;
		*head = new;
		return (*head);
	}
	while (temp->next != NULL)
	{
		if (new->n < temp->next->n)
		{
			new->next = temp->next;
			temp->next = new;
			return (new);
		}
		temp = temp->next;
	}
	temp->next = new;
	return (new);
}
