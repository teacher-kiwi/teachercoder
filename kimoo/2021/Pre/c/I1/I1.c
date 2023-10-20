#include <stdio.h>

int n;
int table[15][15];

int result;
int flag[15];

void p(int now, int value)
{
    int depth = 0;
    for(int i = 0; i < n; i++)
    {
        depth += flag[i];
    }
    if(depth == n)
    {
        if(result < value)
        {
            result = value;
            return;
        }
    }

    for(int i = 1; i < n; i++)
    {
        if(flag[i] == 1)
        {
            continue;
        }

        flag[i] = 1;

        p(i, value+table[now][i]);

        flag[i] = 0;
    }
}

int main()
{
    scanf("%d", &n);

    for(int i = 0; i < n; i++)
    {
        for(int j = 0; j < n; j++)
        {
            scanf("%d", &table[i][j]);
        }
    }

    for(int i = 0; i < n; i++)
    {
        flag[i] = 0;
    }

    flag[0] = 1;
    result = 0;
    p(0, result);

    printf("%d", result);

    return 0;
}