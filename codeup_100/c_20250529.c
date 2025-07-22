1026
#include <stdio.h>

int main()
{
    int h, m, s;
    scanf("%d:%d:%d", &h, &m, &s);
    printf("%d", m);
    return 0;
}


1027
#include <stdio.h>

int main()
{
    int y, m, d;
    scanf("%04d.%02d.%02d", &y, &m, &d);
    printf("%02d-%02d-%04d", d, m, y);
    return 0;
}
