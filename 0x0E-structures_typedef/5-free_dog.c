#include <stdlib.h>
#include "dog.h"

/**
 * free_dog - free space occupied by variable dog
 * @d: pointer to the variable to be freed
 */
void free_dog(dog_t *d)
{
if (d != NULL)
{
free(d->name);
free(d->owner);
free(d);
}
}
