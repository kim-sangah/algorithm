1041
#include <stdio.h>

int main()
{
    char a;
    scanf("%c", &a);
    printf("%c", a + 1);
    return 0;
}


1042
#include <stdio.h>

int main()
{
    int a, b;
    scanf("%d %d", &a, &b);
    printf("%d", (int)(a/b));
    return 0;
}


1043
#include <stdio.h>

int main()
{
    int a, b;
    scanf("%d %d", &a, &b);
    printf("%d", (int)(a%b));
    return 0;
}


1044
#include <stdio.h>

int main()
{
    long long a;
    scanf("%lld", &a);
    printf("%lld", ++a);
    return 0;
}


1045
#include <stdio.h>

int main()
{
    int a, b;
    scanf("%d %d", &a, &b);
    printf("%d\n", a+b);
    printf("%d\n", a-b);
    printf("%d\n", a*b);
    printf("%d\n", int(a/b));
    printf("%d\n", a%b);
    printf("%.2f\n", (float)a/b);
    return 0;
}
