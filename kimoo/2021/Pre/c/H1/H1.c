# include <stdio.h>

int virus(int n, int k)
{   
    if (k < 2) return n;
    if (k == 2) return n + virus(n * 2, k-2);
    if (k > 2) return n + virus(n * 2, k-2) + virus(n, k-3);
}

int main()
{
    int n;
    int k;
    scanf("%d%d", &n, &k);

    int result = virus(n, k);
    printf("%d", result);
}