#ifndef _LISTS_H_
#define _LISTS_H_

#include <stdlib.h>

typedef struct listint_s
{
	int x;
	struct listint_s *next;
} listint_t;
size_t print_listin(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int x);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);

#enif /* LIST_H */
