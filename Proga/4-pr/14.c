#include <stdio.h>

int kolvo(int a) {
    int k = 0;
    for (int i = 0; i < 32; i++) {
        if (a & 1 == 1) {
            k++;
        }
        a = a >> 1;
    }
    return k;
}
int main() {
    int n;
    printf("Введи число: ");
    scanf("%d", &n);
    if (n < 0) {
        printf("Должно быть неотрицательное\n");
    }
    else {
        printf("Количество единиц: %d\n", kolvo(n));
    }

}
