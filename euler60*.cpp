#include <iostream> // jpt vayo.. :( :( :( :( :( :( :( :( :( :(
#include <cmath>
#include "primegen.cpp"
using namespace std;

bool isprime(long n) {
	for(int i=2;i<(int)sqrt((float)n)+1;i++) {
		if(n%i==0)return false;
	}
	return true;
}
bool inarr(int *arr, int val, int len)
{
	int high, low;
	high=len-1;
	low=0;
	int avg=(high+low)/2;
	while(1) {
		if(val==arr[avg])return true;
		if((avg==high or avg==low) and val!=arr[avg])return false;
		if(val<arr[avg]) {
			high=avg;
		}
		else low=avg;
		avg=(high+low)/2;
	}
}


bool isconcatprime(int a, int b)
{
	int temp=(int)log10(b)+1;
	long c=a*pow(10,temp)+b;
	//if(c<100000) if(!inarr(primes, c, total))return false;
	 if(!isprime(c))return false;
	temp=(int)log10(a)+1;
	c=b*pow(10,temp)+a;
	//if(c<100000) if(!inarr(primes, c, total))return false;
	 if(!isprime(c))return false;
	return true;
}


int main()
{
	primegen(1000000);
	int arr[1000000]={0};
	int cnt=0;
	for(int i=0;i<3;i++) {
		for(int j=i+1;j<2;j++) if(isconcatprime(primes[i], primes[j]))cnt++;
	}
	cout << cnt;


}
