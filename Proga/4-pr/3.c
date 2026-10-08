#include <stdio.h>

int chered(int n) {
	if ((n & (n >> 1)) == 0) {
		return 1;
	}
	else {
		return 0;
	}
}

int main() {
	int a;
	scanf("%d", &a);
	if (chered(a)) {
		printf("Чередуются\n");
	}
	else {
		printf("Не чередуются\n");
	}
}
