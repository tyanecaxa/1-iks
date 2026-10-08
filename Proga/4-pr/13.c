#include <stdio.h>

int stepen(int n) {
	int k = 0;
	for (int i = 0; i < 32; i++) {
		if ((n & 1) == 1) {
			k++;
		}
		n = n >> 1;
	}	 
	if (k==1) {
		return 1;
	}
	else {
		return 0;
	}
}

int main() {
	int n;
	printf("Введи число: ");
	scanf("%d", &n);
	if (n < 1) {
                printf("Не натуральное\n");
        }
	else {
		if (n == 1 || stepen(n)) {
			printf("Степень\n");
		}
		else {
			printf("Не степень\n");
		}
	}
}

