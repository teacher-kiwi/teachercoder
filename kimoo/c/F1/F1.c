#include <stdio.h>

int main()
{
    int n;
    float record[1000];
    float target;

    scanf("%d", &n);
    for(int i = 0; i < n; i++)
    {
        scanf("%f", &record[i]);
    }
    scanf("%f", &target);

    float distance[1000];
    for(int i = 0; i < n; i++)
    {
        distance[i] = record[i] - target;
        if(distance[i] < 0) distance[i] *= -1;
    }

    int check = 0;
    for(int i = 0; i < n-1; i++)
    {
        if(distance[check] > distance[i+1]) check = i+1;
    }

    printf("%.2f", record[check]);
}