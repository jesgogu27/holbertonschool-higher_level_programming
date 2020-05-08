#include "lists.h"
/**
 * linkedlist_pal - verify if double list can be palindrome
 * @tmp:  head
 * @h: head of the double list
 * Return: 1 if it is a linked list, 0 if not
 */
int linkedlist_pal(listint_t **nAux, listint_t *h)
{
	if (!h)
		return (1);
	while (linkedlist_pal(nAux, h->next) == 1 && (*nAux)->n == h->n)
	{
		*nAux = (*nAux)->next;
		return (1);
	}
	return (0);
}
/**
 * is_palindrome - checks if a double list is a palindrome
 * @head: head of the double list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	int r;

	if (!head || !*head || !(*head)->next)
		return (1);
	r = linkedlist_pal(head, *head);
	return (r);
}