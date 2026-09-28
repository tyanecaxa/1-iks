#include <stdio.h>

int main(){
float x;
float y;
printf("x,y = ");
scanf("%f, %f", &x, &y);
	if (y <= 0 && y >= -2) {
		if (x >= -1.8 && x <= 1) {
			printf("YES\n");
		}
		else {
			printf("NO\n");
		}
	}
	else if (y <= 1 && y > 0) {
		if (x >= -1.8 && x <= -1) {
			printf("YES\n");
		}
		else if (y <= -x) {
			printf("YES\n");
		}
		else {
			printf("NO\n");
		}
	}
	else {
		printf("NO\n");
	}
return 0;
}

