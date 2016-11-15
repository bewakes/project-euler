// square root convergents
#include <iostream>
#include <cmath>
#define LEN 200
using namespace std;

void multiply(int *arr, int len, int n)
{
	int rem=0;
	for(int i=0;i<len; i++) {
		int c=arr[i]*n +rem;
		arr[i]=c%10000;
		rem=c/10000;
	}
}

void add(int *arr1, int *arr2, int len)
{
	int rem=0;
	int c;
	for(int i=0;i<len; i++) {
		c=arr1[i]+arr2[i]+rem;
		arr1[i]=c%10000;
		rem=c/10000;
	}
}

void copyarr(int *a, int * b, int len=LEN) {
	for(int i=0;i<len;i++)b[i]=0;
	for(int i=0;i<len;i++) {
		b[i]=a[i];
	}
}

void printarr(int *arr, int len=LEN)
{
	for(int i=0;i<len;i++) {
		cout << arr[i]<< " ";
	}
	cout << endl;
}

bool islonger(int *a, int *b, int len=LEN)
{
	int cnta=LEN-1, cntb=LEN-1;
	while(a[cnta]==0)cnta--;
	while(b[cntb]==0)cntb--;
	if(cnta>cntb)return true;
	if(cnta<cntb)return false;
	if(cnta==cntb) {
		//cout << a[cnta] << " "<<b[cntb]<<endl;
		int aa=(int)log10(a[cnta]);
		int bb=(int)log10(b[cntb]);
		if(aa>bb) { return true; }
		else return false;
	}
}

int main()
{
	int num[LEN];
	int den[LEN];
	int temp[LEN];
	for(int x=0;x<LEN;x++) {
		*(num+x)=0;
		*(den+x)=0;
	}
	int totalcnt=0;
	for(int i=1;i<=1000;i++) {
		for(int x=0;x<LEN;x++) {
		*(num+x)=0;
		*(den+x)=0;
	}
		num[0]=1;
		den[0]=1;
		for(int x=1;x<=i;x++) {
			// swap num and den;
			add(num, den, LEN);
			copyarr(num, temp);
			copyarr(den, num);
			copyarr(temp, den);
			add(num, den, LEN);
		}

	if(islonger(num, den))totalcnt++;
	}
	cout << totalcnt;

	return 0;
}
