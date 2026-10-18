#include <stdio.h>

void seria(int cifra[], int lencifra[], int count) {
    for (int i = 0; i < count; i++) {
        if (lencifra[i] > 2) {
        printf("%d %d\n", cifra[i],lencifra[i]);
        }
    }
}

void max(int cifra[],int countcifra[],int count) {
    int mx = 0;
    int c = 0;
    for (int i = 0; i < count; i++) {
        if (countcifra[i] > mx) {
            mx = countcifra[i];
            c = cifra[i];
        }
    }
    printf("%d %d\n",c,mx);
}

int proc(int n, int count) {
    return n/count;
}

void unpack(int cifra[],int countcifra[],int count) {
    for (int i = 0; i < count; i++) {
        for (int j = 0; j < countcifra[i]; j++) {
            if (j == countcifra[i]-1 && cifra[i]==cifra[count-1]) {
                printf("%d}\n",cifra[i]);
            }
            else {
                printf("%d, ",cifra[i]);
            }
        }
    }
}

#define n 22

int main(void) {
    int x[n] = {3,3,3,5,5,6,6,7,9,9,9,7,9,9,2,4,4,4,8,8,8,8};
    int count = 0;
    int cifra[n], countcifra[n];
    int count_xi = 1;
    for (int i = 0; i < n; i++) {
        if (x[i] == x[i+1]) {
            count_xi++;
        }
        else {
            cifra[count] = x[i];
            countcifra[count] = count_xi;
            count += 1;
            count_xi = 1;
        }
    }

    printf("Серии длиннее двух:\n");
    seria(cifra,countcifra,count);

    printf("Самая длинная серия: ");
    max(cifra,countcifra,count);

    printf("Сжалось в %d раза\n", proc(n, count));

    printf("Обратная распаковка: {");
    unpack(cifra,countcifra,count);

}
