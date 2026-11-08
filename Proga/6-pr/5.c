#include <stdio.h>
#include <math.h>

double opred(int n, double m[n][n]) { //по методу Гаусса
    // делаем локальную матрицу
    double o[n][n];
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            o[i][j] = m[i][j];
        }
    }

    double opr = 1;
    int k = 1;

    for (int t = 0; t < n; t++) { //столбцы
        // номер строки с макс по модулю числом в столбце
        int mx = t;
        for (int i = t + 1; i < n; i++) {
            if (fabs(o[i][t]) > fabs(o[mx][t])) { // ниже > макс до этого
                mx = i;
            }
        }

        // если весь остаток столбца равен нулю
        if (fabs(o[mx][t]) < 1e-12) { // макс число в столбце < 1e-12 ~ 0.000000000001
            return 0.0;
        }

        // меняем строки местами
        if (mx != t) { //если макс строка ниже текущего столбца
            for (int j = 0; j < n; j++) { //столбцы
                double temp = o[t][j]; //копируем значение
                //меняем местами значения
                o[t][j] = o[mx][j]; 
                o[mx][j] = temp; 
            }
            k = -k; //меняем знак, потому что при перемещении строк 
                    //определитель меняет знак 
        }

        // опред на диагональ
        opr *= o[t][t];

        // обнуляем элементы ниже диагонали
        for (int i = t + 1; i < n; i++) {
            double factor = o[i][t] / o[t][t]; //частное от деления знач ниже на макс элем

            for (int j = t + 1; j < n; j++) { 
                o[i][j] -= factor * o[t][j]; //вычитаем верхнюю строку от нижней
            }

            o[i][t] = 0; //обнуляем текущий элем ниже макс
        }
    }

    return k*opr;
}


int main() {
    int n; //размер матрицы
    scanf("%d\n", &n);

    // создаем матрицу из ввода с клавиатуры
    double m[n][n];
    for (int r = 0; r < n; r++) {
        for (int c = 0; c < n; c++) {
            scanf("%lf", &m[r][c]);
        }
    }
    // матрица равенства с клавиатуры
    double mr[n];
    for (int i = 0; i < n; i++) {
        scanf("%lf",&mr[i]);
    }

    double x[n]; //значения переменных
    double op = opred(n, m);

    if (op == 0.0) {
        printf("Нет единственного решения\n");
        return -1;

    }
    for (int j = 0; j < n; j++) {
        //копируем матрицу
        double temp[n][n];
        for (int i = 0; i < n; i++) {
            for (int k = 0; k < n; k++) {
                temp[i][k] = m[i][k];
            }
        }

        for (int i = 0; i < n; i++) {
            temp[i][j] = mr[i]; //заменяем столбец текущего икса на равенства
        } 

        double opx = opred(n, temp);
        x[j] = opx / op; //считаем икс и записываем
        if (x[j] == 0.0) { //чтобы не выводился -0.0
            x[j] = 0.0;
        }
    }
    // выведем ответ
        for (int i = 0; i < n; i++) {
        printf("x%d = %.2lf ", i+1, x[i]);
    }
    printf("\n");
 
}