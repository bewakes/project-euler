#include <iostream>
#include <cmath>
using namespace std;

bool isInt(float a)
{
	return(static_cast<int>(a)==a/1.0);
}

int sumDigits(long a)
{
	int sum =0;
	int t;
	while(a){ t = a%10; sum+=t; a/=10; }
	return sum;
}

int main()
{
	float c;int cnt=0;
	for(long i=10;i<999999999;i++) {
		long s = sumDigits(i);
		
		long a = 1;
		for(int j=0;j<30;j++); {
			if(s==1) break;
			a = pow(s, j);
			if(a==i){ cnt++; cout << cnt<<": sum: "<< s<< " power: "<< j<< endl;break;}
			if(a>i)break;
		}
		
		if(s!=1) {
			float c = logl(i)/logl(s);
			//if(isInt(c)) cout << ++cnt<<": sum: "<< s<< " power: "<< c<< endl;
		}
	}
	return 0;
}
