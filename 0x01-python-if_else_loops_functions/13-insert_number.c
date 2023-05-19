#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * insert_node - adds a new node due to number rank
 * @head: pointer to pointer of first node of listint_t list
 * @number: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t	*current = *head;
	listint_t	*next = current->next;
	listint_t	*new;

	if (!head)
		return (NULL);
	if (!next && number > current->n)
	{
		add_nodeint_end(head, number);
		return (current->next);
	}
	if (!next && number < current->n)
	{
		next = *head;
		*head = add_nodeint_end(NULL, number);
		current->next = next;
		return (*head);
	}
	while (next && next->n < number)
	{
		current = current->next;
		next = next->next;
	}
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	current->next = new;
	new->next = next;
	return (new);
}
