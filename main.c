#include <stdio.h>
#include <stdlib.h>

int		main(int argc, char **argv)
{
	float	price_a;
	float	price_b;
	float	mass_a;
	float	mass_b;
	float	diff;
	float	price_per_a;
	float	price_per_b;

	printf("price A: %s\n", argv[1]);
	price_a = atol(argv[1]);
	printf("mass A: %s\n", argv[2]);
	mass_a = atol(argv[2]);
	printf("price B: %s\n", argv[3]);
	price_b = atol(argv[3]);
	printf("mass B: %s\n", argv[4]);
	mass_b = atol(argv[4]);
	price_per_a = price_a / mass_a;
	price_per_b = price_b / mass_b;
	printf("price per A:%.2f\n", price_per_a);
	printf("price per B:%.2f\n", price_per_b);
	printf("\n");
	if (price_per_a < price_per_b)
	{
		diff = price_per_b / (price_per_a / 100) - 100;
		printf("A less than B on %.2f%%\n", diff);
	}
	if (price_per_b < price_per_a)
	{
		diff = price_per_a / (price_per_b / 100) - 100;
		printf("B less than A on %.2f%%\n", diff);
	}
	return (0);
}
