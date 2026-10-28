#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    int matrix[n][n];
    int opred = 0;

    if (n > 1) {
        int num = 1;
        int g = 1;
        int p = 1;
        for (int rows = 0; rows < n; rows++) {
            for (int cols = 0; cols < n; cols++) {
                matrix[rows][cols] = num;
                if (rows == cols) {
                    g *= matrix[rows][cols];
                }
                if (rows + cols == n - 1) {
                    p *= matrix[rows][cols];
                }
                num++;
                printf("%d ", matrix[rows][cols]);
            }
            printf("\n");

        }
        if (n == 2) {
            opred = g - p;
        }
        else if (n == 3) {
            opred = g - p 
            + matrix[0][1]*matrix[1][2]*matrix[2][0]
            + matrix[0][2]*matrix[1][0]*matrix[2][1]
            - matrix[0][0]*matrix[1][2]*matrix[2][1]
            - matrix[0][1]*matrix[1][0]*matrix[2][2];
        }
    }
    else {
        opred = 0;
    }
    printf("%d\n", opred);
}