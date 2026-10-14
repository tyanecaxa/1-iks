#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    int n;
    scanf("%d",&n);
    srand(time(NULL));

    int m[n];
    for (int i = 0; i < n; i++) {
        m[i] = -32768 + rand() % (32767 + 32768 +1);
    }

    int sum = 0;
    int max = -32769;
    int maxi = 0;
    for (int i = 0; i < n-1; i += 2) {
        printf("m[%d] = %d + j*(%d)\n", i, m[i], m[i+1]);
        if (max < m[i]) {
            max = m[i];
            maxi = i;
        }
        sum += m[i]*m[i]+m[i+1]*m[i+1];
    }
    printf("sum = %d, max re = %d, max ire = %d\n", sum, max, maxi);
}