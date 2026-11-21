#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>


// Движение песка
void move_sand(int **field, int N, int M) {

    for (int i = N - 2; i >= 0; i--) {
        int lf = rand() % 2;
        for (int st = 0; st < M; st++) {
            int j = lf ? st : (M - 1 - st);

            if (field[i][j] == 1) {

                // Движение вниз
                if (field[i + 1][j] == 0) { //воздух
                    field[i + 1][j] = 1;
                    field[i][j] = 0;
                }
                else if (field[i + 1][j] == 3) { //вода
                    field[i + 1][j] = 1;
                    field[i][j] = 3;
                }

                else {
                    int direction = (rand() % 2) ? -1 : 1;
                    int f = j + direction;
                    int sc = j - direction;

                    if (f >= 0 && f < M && (field[i+1][f] == 0 || field[i+1][f] == 3)) {
                        field[i][j] = field[i+1][f];
                        field[i+1][f] = 1;
                    }
                    else if (sc >= 0 && sc < M && (field[i+1][sc] == 0 || field[i+1][sc] == 3)){
                        field[i][j] = field[i+1][sc];
                        field[i+1][sc] = 1;
                    }
                }
            }
        }
    }
}

// Движение воды
void move_water(int **field, int N, int M) {
    
    for (int i = N - 2; i >= 0; i--) {
        for (int j = 0; j < M; j++) {
            if (field[i][j] == 3) {
                int moved = 0;

                // движение вниз
                if (field[i + 1][j] == 0) {
                    field[i + 1][j] = 3;
                    field[i][j] = 0;
                    moved = 1;
                }
                // движение по диагонали
                else {
                    if (j < M - 1 && field[i][j + 1] == 0) {
                        field[i][j + 1] = 3;
                        field[i][j] = 0; 
                        moved = 1;
                    }
                    if (j > 0 && field[i][j - 1] == 0) {
                        field[i][j - 1] = 3;
                        field[i][j] = 0;
                        moved = 1;
                    }

                    // Движение по горизонтали
                    if (moved == 0) {
                        if (j > 0 && field[i][j - 1] == 0) {
                            field[i][j - 1] = 3;
                            field[i][j] = 0;
                        }

                        if (j < M - 1 && field[i][j + 1] == 0) {
                            field[i][j + 1] = 3;
                            field[i][j] = 0;
                        }
                    }            
                }
            }
        }
    }
}

#define RESET  "\033[0m"
#define YELLOW "\033[33m"
#define GRAY   "\033[90m"
#define BLUE   "\033[34m"
// Вывод поля
void print_field(int **field, int N, int M) {

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {

            if (field[i][j] == 0) {
                printf(".");
            }
            else if (field[i][j] == 1) {
                printf(YELLOW "#" RESET);
            }
            else if (field[i][j] == 2) {
                printf(GRAY "X" RESET);
            }
            else if (field[i][j] == 3) {
                printf(BLUE "~" RESET);
            }
        }

        printf("\n");
    }
}

int main(int argc, char *argv[]) {

    // Проверка аргументов
    if (argc != 3) {
        printf("Usage: %s N M\n", argv[0]);
        return 1;
    }
    int N = atoi(argv[1]);
    int M = atoi(argv[2]);
    if (N <= 0 || M <= 0) {
        printf("Invalid field size\n");
        return 1;
    }

    srand(time(NULL));

    // Выделение динамической памяти
    int **field = malloc(N * sizeof(int *));

    if (field == NULL) {
        return 1;
    }

    for (int i = 0; i < N; i++) {
        field[i] = calloc(M, sizeof(int));

        if (field[i] == NULL) {
            for (int k = 0; k < i; k++) {
                free(field[k]);
            }
            free(field);
            return 1;
        }
    }

    // Создание препятствий
    for (int i = 2; i < N; i++) {
        for (int j = 0; j < M; j++) {
            if (rand() % 100 < 5) {
                field[i][j] = 2;
            }
        }
    }

    clock_t start = clock();
    // Симуляция
    for (int frame = 0; frame < 20; frame++) {

        // Появление нового песка/воды сверху
        for (int j = 0; j < M; j++) {
            if (field[0][j] == 0) {
                int mat = rand() % 10;
                if (mat < 3) {
                    field[0][j] = 1; //песок
                }
                else if (mat == 3) {
                    field[0][j] = 3; //вода
                }
            }
        }

        // Движение песка/воды
        move_sand(field, N, M);
        move_water(field, N, M);
        // Очистка терминала
        printf("\033[H\033[J");
        // Вывод нового кадра
        print_field(field, N, M);
        usleep(1000000);
    }

    clock_t end = clock();
    double seconds = (double)(end - start) / CLOCKS_PER_SEC;
    printf("Time: %.3f seconds\n", seconds);

    // Освобождение памяти
    for (int i = 0; i < N; i++) {
        free(field[i]);
    }
    free(field);

    return 0;
}

// 25.166 sec