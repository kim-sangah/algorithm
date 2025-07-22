1024
#include <stdio.h>

int main()
{
    char d[30];
    int i;
    scanf("%s", d);
    for(i=0; d[i]!='\0'; i++)
        printf("\'%c\'\n", d[i]);
    return 0;
}


1025
#include <stdio.h>

int main()
{
    int a, b, c, d, e;
    scanf("%1d%1d%1d%1d%1d", &a, &b, &c, &d, &e);
    printf("[%d]\n", a*10000);
    printf("[%d]\n", b*1000);
    printf("[%d]\n", c*100);
    printf("[%d]\n", d*10);
    printf("[%d]\n", e);
    return 0;
}
