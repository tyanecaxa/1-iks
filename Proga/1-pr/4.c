#include <stdio.h>

int main() {
float g;
char t;
printf("Input temperature:");
scanf("%f%c", &g, &t);
if (t == 'c' || t == 'C') {
g = (g * 9/5) + 32;
printf("Ouput temperature:%.1f%c\n",g, 'f');
}
else if (t == 'f' || t == 'F') {
g = (g - 32) * 5/9;
printf("Ouput temperature:%.1f%c\n",g, 'c');
}
else {
printf("Ouput error\n");
}
return 0;
}
