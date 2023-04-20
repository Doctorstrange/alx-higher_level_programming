#include <stdio.h>
#include "function_pointers.h"
/**
 * int_index - function that prints a name
 * @array: array to check for int
 * @size: the size of the array
 * @cmp: the function that runs the comparism
 * Return: the index of the match integer
 */
int int_index(int *array, int size, int (*cmp)(int))
{
int x;
if (array == NULL || cmp == NULL)
return (-1);

if (size <= 0)
return (-1);

for (x = 0; x < size; x++)
{
if (cmp(array[x]) != 0)
{
return (x);
}
}
return (-1);
}
