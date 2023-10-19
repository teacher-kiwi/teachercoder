#include <stdio.h>

int main()
{
    int n;
    int m;
    scanf("%d %d", &n, &m);

    int map[10][10];
    for(int i=0; i<n; i++)
    {
        for(int j=0; j<m; j++)
        {
            if(i==0) map[i][j] = 1;
            else
            {
                if(j==0) map[i][j] = 1;
                else
                {
                    map[i][j] = map[i-1][j] + map[i][j-1];
                }
            }
        }
    }

    printf("%d", map[n-1][m-1]);
}