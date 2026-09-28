#include <stdio.h>

int main() {
	long long e;
	long long n;
	long long message;
	printf("Открытый ключ/Модуль/Сообщение: ");
	scanf("%lld %lld %lld", &e, &n, &message);

	long long p;
	long long q;
	for (long long i = 2; i < n; i++) {
		if (n % i == 0) {
			p = i;
			q = n/i;
			break;
		}
	}

	long long fi = (p - 1)*(q - 1);
	long long d;
	for (long long i = 1; 1; i++) {
		if ((i*e) % fi == 1) {
			d = i;
			break;
		}
	}

	long long symb = 1;
	for (long long i = 0; i < d; i++) {
		symb = (symb * message) % n;
	}

	printf("Шифр: %lld\n", symb);
	return 0;
}
