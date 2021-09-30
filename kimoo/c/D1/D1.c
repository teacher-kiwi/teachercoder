#include <stdio.h>

int nSum(int number)
{
    int sum = 0;
    int checkNum = number;
    while(checkNum)
    {
        sum += checkNum % 10;
        checkNum /= 10;
    }
    return sum;
}

int main()
{
    int k;
    int n;

    scanf("%d %d", &k, &n);

    int num = 0;
    int count = 0;
    while(count < n)
    {
        num++;
        if(nSum(num) == k) count++;
    }

    printf("%d", num);
}