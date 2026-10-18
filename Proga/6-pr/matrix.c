#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    int matrix[n][n];
    float opred = 0;
    for (int rows = 0; rows < n; rows++) {
        for (int cols = 0; cols < n; cols++) {
            matrix[rows][cols] = rows + cols + 1;
            printf("%d ", matrix[rows][cols]);
        }
        printf("\n");
    }
}