#include "lists.h"
/**
 * check_cycle - cycle black and white
 * @list: pointer to head
 * Return: 1 on success, 0 otherwise.
 */
int check_cycle(listint_t *list)
{
	listint_t *black;
	listint_t *white;

	if (list == NULL)
		return (0);
	black = list;
	white = list;

	do {
		black = black->next;
		white = white->next->next;
		if (black == white)
		{
			black = list;
			do {
				black = black->next;
				white = white->next;
			} while (black != white);
			return (1);
		}
	} while (white->next != NULL && white->next->next != NULL);

	return (0);
}
