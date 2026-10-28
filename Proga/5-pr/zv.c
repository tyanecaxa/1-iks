#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    int sp[n][n];

    int top = 0, bottom = n - 1, left = 0, right = n - 1;
    int num = 1;

    while (top <= bottom && left <= right) {
        for (int j = left; j <= right; j++) {
            sp[top][j] = num;
            num++;
        }
        top++;
        
        for (int j = top; j <= bottom; j++) {
            sp[j][right] = num;
            num++;
        }
        right--;

        for (int j = right; j >= left; j--) {
            sp[bottom][j] = num;
            num++;
        }
        bottom--;

        for (int j = bottom; j >= top; j--) {
        sp[j][left] = num;
        num++;
        }
        left++;
    }

    for (int j = 0; j < n; j++) {
        for (int i = 0; i < n; i++) {
            printf("%02d ", sp[j][i]);
        }
        printf("\n");
    }

}