# include <stdio.h>

int main()
{

    long long n;
    long long m;
    scanf("%lld %lld", &n, &m);

    long long bread = n * m;

    if(bread == 0) bread = 0;
    else if(0 < bread && bread <= 30) bread = 30;
    else if(30 < bread && bread <= 50) bread = 50;
    else if(50 < bread && bread <= 60) bread = 60;
    else if(60 < bread && bread <= 80) bread = 80;
    else
    {
        if(bread % 10 == 0) bread = bread;
        else
        {
            bread = bread - (bread % 10) + 10;
        }
    }

    printf("%lld", bread * 300);
}