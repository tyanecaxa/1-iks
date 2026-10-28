#include <stdio.h>

#define n 3

int main() {
    // Записываем данные матрицы
    // scanf("%d", &n);
    double mtr[n][n+1] = {
    {1,2,3,5},
    {4,5,6,8},
    {7,8,0,2}
    };

    // for (int r = 0; r < n; r++) {
    //     for (int c = 0; c < n+1; c++) {
    //         scanf("%lf", &mtr[r][c]);
    //     }
    // }

    // Ищем определитель матрицы в зависимости от N
    int o = 0;
    if (n == 2) {
        int g = 1;
        int p = 1;
        for (int i = 0; i < n; i++) {
            g *= mtr[i][i];
            p *= mtr[i][n-i-1];
        }
        o = g - p;
    }
    if (n == 3){
        int g = 1;
        int p = 1;
        for (int i = 0; i < n; i++) {
            g *= mtr[i][i];
            p *= mtr[i][n-i-1];
        }

        o = g + mtr[0][1]*mtr[1][2]*mtr[2][0] 
        + mtr[0][2]*mtr[2][1]*mtr[1][0]
        - p - mtr[0][0]*mtr[1][2]*mtr[2][1] 
        - mtr[0][1]*mtr[1][0]*mtr[2][2];
        
    }
    printf("%d\n",o);
    
    // ищем определитель переменных
    // перемен. х1
    double ox1 = 0;

    ox1 += mtr[0][3]*mtr[1][1]*mtr[2][2]
    + mtr[0][1]*mtr[1][2]*mtr[2][3]
    + mtr[0][2]*mtr[1][3]*mtr[2][1];
    ox1 -= mtr[2][3]*mtr[1][1]*mtr[0][2]
    + mtr[2][1]*mtr[1][2]*mtr[0][3]
    + mtr[2][2]*mtr[1][3]*mtr[0][1];

    double x1 = ox1/o;
    printf("x1 = %.0f, ", x1);

    // перемен. х2
    
    return 0;
}