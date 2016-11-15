#include <iostream>
#include <cmath>
using namespace std;

bool notsquare(int i)
{
	float s = sqrtf(i);
	if(s==(int)s) return false;
	return true;
}

long p(int D, int n) { // find nth convergent numerator of sqrt of D
	if(n==0) return a(D, 0);
	if(n==1) return a(D, 0)*a(D, 1) + 1;
	return a(D, n)*p(D, n-1) + p(D, n-2);
}

int main()
{
	for(int D=2;D<1000;d++) {
		int cnt = 0;
		if(notsquare(D)){
			a0 = int(sqrtf(D));
			p = a0;

		}
	}
}

