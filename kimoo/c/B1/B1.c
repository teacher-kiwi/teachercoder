#include <stdio.h>

int main()
{
    long long n;
    scanf("%lld", &n);
    if(n == 1) printf("%d", 1);
    else
    {
        printf("%lld", n * (n-1));
    }
}