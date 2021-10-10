#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void reverse(char arr[])
{
    for (int i = 0; i < strlen(arr) / 2; i++)
    {
        char temp = arr[i];
        arr[i] = arr[strlen(arr) - i - 1];
        arr[strlen(arr) - i - 1] = temp;
    }
}

void substruct(char arr1[], char arr2[], char result[])
{
    int length = strlen(arr1) > strlen(arr2) ? strlen(arr1) : strlen(arr2);

    // 빼는 값이 더 큰지 확인
    int bigger = strlen(arr1) >= strlen(arr2) ? 1 : 0;
    if (strlen(arr1) == strlen(arr2))
    {
        for (int i = 0; i < length; i++)
        {
            if (arr1[length - i - 1] < arr2[length - i - 1])
            {
                bigger = 0;
                break;
            }
        }
    }

    int carry = 0;

    // 빼는 값이 작으면
    if(bigger)
    {
        for (int i = 0; i < length; i++)
        {
            int diff = arr1[i] - '0' - arr2[i] - '0' - carry;
            while (diff < -10) diff += '0';
            carry = diff < 0 ? 1 : 0;
            result[i] = diff < 0 ? 10 + diff + '0' : diff + '0';
        }
    }
    // 빼는 값이 더 크면
    else
    {
        for (int i = 0; i < length; i++)
        {
            int diff = arr2[i] - '0' - arr1[i] - '0' - carry;
            while (diff < -10) diff += '0';
            carry = diff < 0 ? 1 : 0;
            result[i] = diff < 0 ? 10 + diff + '0' : diff + '0';
        }
    }

    // 불필요한 0 제거
    for (int i = 0; i < length; i++)
    {
        if(result[length - i - 1] == '0') result[length - i - 1] = 0;
        else break;
    }

    // 빼는 값이 더 컸다면 음수부호 추가
    if (!bigger) strcat(result, "-");
}

void add(char arr1[], char arr2[], char result[])
{
    int length = strlen(arr1) > strlen(arr2) ? strlen(arr1) : strlen(arr2);

    int carry = 0;

    for (int i = 0; i < length; i++)
    {
        int sum = arr1[i] - '0' + arr2[i] - '0' + carry;
        while (sum < 0) sum += '0';
        carry = sum > 9 ? 1 : 0;
        result[i] = sum > 9 ? sum - 10 + '0' : sum + '0';
    }

    if (carry == 1) result[length] = '1';
}

int main()
{
    char a[400] = { 0 };
    char b[400] = { 0 };
    char result[400] = { 0 };

    int scan = scanf("%s%s", a, b);
    if(scan){}

    int c;
    if (a[0] == '-' && b[0] == '-') //b-a
    {
        reverse(a);
        reverse(b);
        a[strlen(a) - 1] = 0;
        b[strlen(b) - 1] = 0;
        c = 0;
    }
    else if (a[0] != '-' && b[0] != '-') //a-b
    {
        reverse(a);
        reverse(b);
        c = 1;
    }
    else if (a[0] == '-' && b[0] != '-') // -(a+b)
    {
        reverse(a);
        reverse(b);
        a[strlen(a) - 1] = 0;
        c = 2;
    }
    else if (a[0] != '-' && b[0] == '-') // a+b
    {
        reverse(a);
        reverse(b);
        b[strlen(b) - 1] = 0;
        c =3;
    }

    switch(c)
    {
        case 0:
            substruct(b, a, result);
            break;
        case 1:
            substruct(a, b, result);
            break;
        case 2:
            add(a, b, result);
            strcat(result, "-");
            break;
        case 3:
            add(a, b, result);
            break;
    }
    reverse(result);

    if (strlen(result) == 0) printf("%d", 1);
    else printf("%ld", strlen(result));

    return 0;
}