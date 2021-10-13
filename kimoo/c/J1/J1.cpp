#include <stdio.h>
#include <queue>
using namespace std;

int main()
{
    int n;
    int m;
    int world[105][105] = {0};
    int check[105][105];

    std::queue< int > q;

    scanf("%d %d", &n, &m);

    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= m; j++)
        {
            scanf("%1d", &world[i][j]);

            if (world[i][j] == 3) q.push(i * (m + 1) + j);
            else if(world[i][j] == 1) check[i][j] = -1;
        }
    }

    int position, count;
    int x, y, xx, yy;
    int dx[4] = {1, -1, 0, 0};
    int dy[4] = {0, 0, 1, -1};
    while(!q.empty())
    {
        position = q.front() % 100000;
        x = position / (m + 1);
        y = position % (m + 1);

        count = q.front() / 100000;
        q.pop();

        if (x<1 or y<1 or x>n or y>m) break;

        for (int k = 0; k < 4; k++)
        {
            xx = x+dx[k];
            yy = y+dy[k];

            if (!check[xx][yy])
            {
                check[xx][yy] = count + 1;
                q.push(xx * (m + 1) + yy + (count + 1) * 100000);
            }
        }
    }
    printf("%d", count);
}