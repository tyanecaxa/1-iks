#include <stdio.h>

int main() {
int n;
printf("Введи число: ");
scanf("%d", &n);
	for (int s = 1, i = 0; i <= n; i++) {
		printf("s: %d i: %d\n", s, i);
		s = s * 2;
	}
}
