#include<stdio.h>

int main()
{
    int i = 0;
    int sum = 0;
    for( i = 0; i < 1000; i++)
    {
        if(i % 3 == 0 || i % 5 == 0)
        {
            sum = sum + i;
        }
    }
    printf("The sum of multiples of 3 or 5 below 1000 is  %d", sum);
    return 0;
}