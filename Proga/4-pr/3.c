#include <stdio.h>

int chered(int a) {
	int k = 0;
	for (int i=0; i < 32; i++) {
		if (a & 1 == 1) {
			k++;
		}
		else {
			k--;
		}
		if (k < -1) {
			return 0;
			break;
		}
		a = a >> 1;
	}

	if (k == 0) {
		return 1;
	}
}

int main() {
	int a;
	scanf("%d", &a);
	printf("%d\n", chered(a));

	
}
