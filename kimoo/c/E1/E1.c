#include <stdio.h>

int main()
{
    int world[100][100];
    int worldSize[2];
    int target[2];
    int n;
    int block[5000][2];
    scanf("%d %d %d %d", &worldSize[0], & worldSize[1], &target[0], &target[1]);
    scanf("%d", &n);
    for(int i = 0; i < n; i++)
    {
        scanf("%d %d", &block[i][0], &block[i][1]);
    }

    for(int i = 0; i < worldSize[0]; i++) //-1로 월드 그리기
    {
        for(int j = 0; j < worldSize[1]; j++)
        {
            world[i][j] = -1;
        }
    }

    for(int i = 0; i < n; i++) //-2로 장애물 그리기
    {
        world[block[i][0]-1][block[i][1]-1] = -2;
    }

    world[0][0] = 0;
    int x[4] = {1, -1, 0, 0};
    int y[4] = {0, 0, 1, -1};

    int count = 0;
    while(1)
    {
        int check = 0;
        for(int i = 0; i < worldSize[0]; i++)
        {
            for(int j = 0; j < worldSize[1]; j++)
            {
                if(world[i][j] == count)
                {
                    for(int k = 0; k < 4; k++)
                    {
                        if(i + x[k] < 0 || i + x[k] >= worldSize[0]) continue;
                        if(j + y[k] < 0 || j + y[k] >= worldSize[1]) continue;
                        if(world[i + x[k]][j + y[k]] == -1)
                        {
                         world[i + x[k]][j + y[k]] = count+1;
                         check++;
                        }
                        if(i + x[k] == target[0]-1 && j + y[k] == target[1]-1)
                        {
                            printf("%d", world[i + x[k]][j + y[k]]);
                            return 0;
                        }
                    }
                }
            }
        }
        if(check == 0)
        {
            printf("%d", world[target[0]-1][target[1]-1]);
            return 0;
        }
        count++;
    }

}