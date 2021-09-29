#include <stdio.h>

int N;
int M;
int map[100][100];
float area = 0;

int main()
{
    scanf("%d %d", &N, &M);
    for(int i = 0; i < N; i++)
    {
        for(int j = 0; j < M; j++)
        {
            scanf("%1d", &map[i][j]);
        }
    }

    for(int i = 0; i < N; i++)
    {
        float n1 = 0;
        float n2 = 100;
        for(int j = 0; j < M; j++)
        {
            if(map[i][j])
            {
                if(n1 < j) n1 = j;
                if(n2 > j) n2 = j;
            }
        }
        if(n1 == 0 || n1 == n2)
        {
         continue;
        }

        for(int j = 0; j < N; j++)
        {
            if(i == j) continue;
            for(int k =0; k < M; k++)
            {
                if(map[j][k])
                {
                    float a = (n1 - n2) * (i - j) / 2;
                    if(a < 0) a *= -1;
                    if(area < a) area = a;
                }
            }
        }
    }

    for(int i = 0; i < M; i++)
    {
        float n1 = 0;
        float n2 = 100;
        for(int j = 0; j < N; j++)
        {
            if(map[j][i])
            {
               if(n1 < j) n1 = j;
               if(n2 > j) n2 = j;
            }
        }
        if(n1 == 0 || n1 == n2) continue;

        for(int j = 0; j < M; j++)
        {
            if(i == j) continue;
            for(int k =0; k < N; k++)
            {
                if(map[k][j])
                {
                    float a = (n1 - n2) * (i - j) / 2;
                    if(a < 0) a *= -1;
                    if(area < a) area = a;
                }
            }
        }
    }

    printf("%.1f", area);
}