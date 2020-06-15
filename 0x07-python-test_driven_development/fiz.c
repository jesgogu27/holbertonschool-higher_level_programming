#include <stdio.h>
#include <string.h>

int main()
{
	int i = 1;

	for (; i < 101; i++)
	{
		if (i % 3 == 0)
		{
			printf("Fizz ");
		}
		else
			{ 
				if(i % 5 == 0)
					printf("Buzz ");
				else
					if((i % 3 == 0) && (i % 5 == 0))
						printf("FizzBuzz ");
					else
						printf("%d ", i);
			}

	}
return (0);
}n