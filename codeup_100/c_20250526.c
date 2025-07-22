1017
#include <stdio.h>

int main()
{
    int a;
    scanf("%d", &a);
    printf("%d %d %d", a, a, a);
    return 0;
}


1018
#include <stdio.h>

int main()
{
    int h, m;
    scanf("%d:%d", &h, &m);
    printf("%d:%d", h, m);
    return 0;
}


1019
#include <stdio.h>

int main()
{
    int y, m, d;
    scanf("%d.%d.%d", &y, &m, &d);
    printf("%04d.%02d.%02d", y, m, d);
    return 0;
}


1020
#include <stdio.h>

int main()
{
    int a, b;
    scanf("%d-%d", &a, &b);
    printf("%06d%06d", a, b);
    return 0;
}
