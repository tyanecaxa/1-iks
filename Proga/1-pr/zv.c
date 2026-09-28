#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int main() {
double height = 600;
double vmks = 7.56;
double f0 = 2.18*pow(10,9);
double REarth = 6371;
double angle;
double c = 299792.458;

printf("Enter elevation angle alpha (0..90 degrees): ");
scanf("%lf", &angle);
	if (0 <= angle && angle <= 90) {
		double angleR = angle * (M_PI / 180);
		double dist = sqrt((pow(REarth,2)*pow(sin(angleR),2) + 2*REarth*height + pow(height,2))) - (REarth*sin(angleR));
		double vR = (vmks*REarth*cos(angleR)) / (REarth*sin(angleR)+dist);
		double delT = (vR*pow(10,9)) / c;
		double angleB = vR / c;
		double fd = (f0*sqrt((1+angleB)/(1-angleB))-f0) / 1000;

		printf("Distance: %.2lf km\n", dist);
		printf("Radial velocity (vr): %.2lf m/s\n", vR*1000);
		printf("Time drift (dt): %.4lf ns/s\n", delT);
		printf("Doppler shift (fd): %.4lf kHz\n", fd);

		printf("PROFILE: ");
		if ((fd > 42 || delT > 18) && (dist > 1000)) {
			printf("CRITICAL ERROR\n");
		}
		else if (fd > 25 && delT > 10) {
			printf("HIGH DYNAMIC MODE\n");
		}
		else if (fd > 3 || fabs(delT) > 1) {
			printf("NORMAL ACCELERATION\n");
		}
		else {
			printf("ZENITH MODE\n");
		}
	}
	else {
		printf("ERROR: angle must be between 0 and 90 degrees.\n");
	}
return 0;
}

