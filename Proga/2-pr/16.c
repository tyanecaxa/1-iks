#include <stdio.h>

int main() {
int a;
printf("Введи число: ");
scanf("%d", &a);
	for (int i=2; i<a; i++) {
		if (a%i==0) {
			printf("a: %d i: %d\n", a, i);
			break;
		}
		if (i==a) {
			puts("Good");
		}
	}
}
