#include <stdio.h>

int main() {
	int h;
	printf("Высота фигуры: ");
	scanf("%d", &h);

	for (int i = 1; i <= h; i++) {
		if (i == 1 || i == h) {
			for (int g = 1; g <= h; g++) {
				printf("*");
			}
			printf("\n");
		}
		else if (i > 1) {
			for (int j = 1; j <= h; j++) {
				if (j == 1 || j == h) {
					printf("*");
				}
				else if (j > 1) {
					printf(" ");
				}
			}
			printf("\n");
		}
	}

}
