#include <stdio.h>
#include "main.h"
/**
 * print_binary - function that prints the binary representation of a number
 * @n: number to derive representation
 * Return: nothing
 */
void print_binary(unsigned long int n)
{
int x;

for (x = (sizeof(unsigned long int) * 8) - 1; x >= 0; x--)
{
if ((n >> x) & 1)
putchar('1');
else
putchar('0');
}
}
