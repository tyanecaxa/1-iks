#include <stdio.h>

int main() {
int a;
printf("Введи число: ");
scanf("%d", &a);
	for (int s = 0, n = 2; n<a; n++) {
		if (a%n==0) {
			s++;
			printf("s: %d n: %d\n", s, n);
		}
		if (s==0) {
			puts("Good");
		}
	}
}
