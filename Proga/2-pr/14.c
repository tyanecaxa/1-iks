#include <stdio.h>

int main() {
int a;
printf("Введи число: ");
scanf("%d", &a);
for (int n = 2; n < a; n++) {
	if (a%n==0) {
		printf("a: %d n: %d\n", a, n);
		break;
	}
	if (n == a) {
		puts("Good");
	}
}
}
