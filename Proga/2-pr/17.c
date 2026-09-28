#include <stdio.h>

int main() {
int b;
printf("Введи число: ");
scanf("%d", &b);
int n=2, flag = 0;
	while ( b % n != 0) {
		n++;
		printf("b: %d n: %d flag: %d\n", b, n, flag);
		if (n==b) {
			flag = 1;
                        printf("b: %d n: %d flag: %d\n", b,n,flag);
			break;
		}
	}

}

