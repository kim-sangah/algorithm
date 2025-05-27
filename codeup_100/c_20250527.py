1021
#include <stdio.h>

int main()
{
    char data[51]="";
    scanf("%s", data);
    printf("%s", data);
    return 0;
}


1022
#include <stdio.h>

int main()
{
    char data[2001];
    fgets(data, 2000, stdin);
    scanf("%s", data);
    printf("%s", data);
    return 0;
}


1023
#include <stdio.h>

int main()
{
    int a, b;
    scanf("%d.%d", &a, &b);
    printf("%d\n%d", a, b);
    return 0;
}
