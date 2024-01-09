#include "lists.h"

/**
 * check_node_length - Function to calculate the length of the linked list.
 * @head: A pointer to the head of the linked list.
 * Return: Returns the length of the linked list.
 */
int check_node_length(listint_t **head)
{
	listint_t *temp = *head;
	int length = 0;

	while (temp != NULL)
	{
		length++;
		temp = temp->next;
	}
	return (length);
}

/**
 * move_to - Function to move to a specific node in the linked list.
 * @node: The index of the node to move to.
 * @head: A pointer to the head of the linked list.
 * Return: a pointer to the node at the specified index.
 */
listint_t *move_to(int node, listint_t **head)
{
	listint_t *temp = *head;

	if (*head == NULL)
		return (NULL);
	while (node > 1)
	{
		temp = temp->next;
		node--;
	}
	return (temp);
}

/**
 * is_palindrome - Function to check if a linked list is a palindrome.
 * @head - A pointer to the head of the linked list.
 * Return: 1 if the linked list is a palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
	int middle_node = check_node_length(head) / 2 + check_node_length(head) % 2;
	int move = check_node_length(head) - middle_node;
	listint_t *alt_temp = NULL, *temp = NULL;

	if (*head == NULL)
		return (0);
	if (check_node_length(head) == 1)
		return (1);
	while (move > 0)
	{
		temp = move_to(middle_node + move, head);
		if (check_node_length(head) % 2 == 0)
			alt_temp = move_to(middle_node - move + 1, head);
		else
			alt_temp = move_to(middle_node - move, head);
		if (temp->n != alt_temp->n)
			return (0);
		move--;
	}
	return (1);
}
