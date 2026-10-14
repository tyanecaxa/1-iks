#include <stdio.h>

void seria(int cifra[], int lencifra[], int count) {
    for (int i = 0; i < count; i++) {
        printf("%d %d", cifra[i],lencifra[i]);
    }
    printf("\n");
}

void anpack(int cifra[],int countcifra[],int count,int anp[],int n) {
    n = 0;
    for (int i = 0; i < count; i++) {
        for (int j = 0; j < countcifra[i]; j++) {
            anp[n++] = cifra[i];
        }
    }
}

int main(void) {
    int x[20] = {3,3,3,3,7,7,9,9,9,9,9,9,2,4,4,4,8,8,8,8};
    int cifra[], countcifra[];
    int count = 0;
    int count_xi = 1;
    for (int i = 0; i < 20; i++) {
        if (x[i] == x[i+1]) {
            count_xi++;
        }
        else {
            cifra[count] = x[i];
            countcifra[count+1] = count_xi;
            count += 2;
            count_xi = 1;
        }
    }
    printf("Серии длиннее двух:\n");
    seria(cifra,countcifra,count);

    int maxl = 0;
    for (int i = 0; i < count; i++) {
        
    }
    int nmaxl = 0;
    int kp = 0;

    printf("nmaxl: %d\n",nmaxl);
    printf("delta: %d\n", 40/kp);

    // for (int i = 0; i < kp; )
}