#include <stdio.h>

int main() {
	int a;
	int n;
	scanf("%d", &a);
	for (int i; i < sizeof(a)-1; i++) {
		if (a >> i == 1) {
			a += 1;
		}
		else {
			a -= 1;
		}
	}

if (n == 0) {
	printf("Чередуется\n");
}
else {
	printf("Не чередуется\n");
}

}
