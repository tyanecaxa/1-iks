#include <stdio.h>

int perv1(int a) {
    int k = 0;
    for (int i = 0; i < 32; i++) {
        k++;
        if (a & 1 == 1) {
            break;
        }
        a = a >> 1;
    }
    return k;
}

int main() {
    int a;
    scanf("%d",&a);
    printf("%d\n", perv1(a));
}