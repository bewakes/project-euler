#include <iostream>
using namespace std;

int gcd(int a, int b)
{
	if(a%b==0)return b;
	else return gcd(b, a%b);
}

int main()
{
	int mxm = 8;
	int num1, num2, den1, den2;
	num1 = 3;den1 = 7; num2 = 1; den2 = 3;int num, den;
	int tempn=num1+num2, tempd = den1+den2;
	int c = gcd(tempn, tempd);
	tempn/=c;tempd/=c;
	num2 = tempn; den2 = tempd;
	int soln,sold;
	while(1) {
		num = num1+num2;
		den = den1+den2;
		c = gcd(num, den);
		num/=c; den/=c;
		if(c!=1){
			if(num==tempn and den==tempd)break;
			tempn = num+num1;tempd = den+den1;
			num=tempn+num1; den = tempd+den1;
			c=gcd(num,den);
			num/=c;den/=c;
			num2=num;den2=den;
		}
		if(num==tempn and den==tempd)break;
		if(den<mxm) {
			soln = num;sold=den;
			tempn=num1+num2, tempd = den1+den2;
			c = gcd(tempn, tempd);
			tempn/=c;tempd/=c;
		}
	}
	cout << num2 << " **** "<< den2;
}
