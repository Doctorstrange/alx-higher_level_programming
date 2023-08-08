#include <stdio.h>
#include <stdlib.h>
#include "lists.h"


int check_cycle(listint_t *list) {
    listint_t *x = list, *y = list;

    while (x != NULL && y != NULL && y->next != NULL) {
        x = x->next;
        y = y->next->next;
        if (x == y) {
		return (1);
        }
    }

    return (0);
}
