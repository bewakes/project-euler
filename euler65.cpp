// convergents of e
#include <iostream>
#include <cmath>
#define LEN 400
using namespace std;

int sum(int n)
{
	int s=0;
	while(n)
	{
		s+=n%10;
		n/=10;
	}
	return s;
}

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

void copyarr(int *b, int * a, int len=LEN) {
	for(int i=0;i<len;i++)b[i]=0;
	for(int i=0;i<len;i++) {
		b[i]=a[i];
	}
}

void printarr(int *arr, int len=LEN)
{
	int i=len-1;
	while(arr[i]==0)i--;
	for(int k=i;k>=0;k--) {
		cout << arr[k]<< " ";
	}
	cout << endl;
}

bool islonger(int *a, int *b, int len=LEN)
{
	int cnta=LEN-1, cntb=LEN-1;
	while(a[cnta]==0)cnta--; while(b[cntb]==0)cntb--;
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
	int num[LEN]={0};
	int den[LEN]={0};
	int temp[LEN]={0};
	int temp1[LEN]={0};
	int i=100;
		for(int x=0;x<LEN;x++) {
		*(num+x)=0;
		*(den+x)=0;
		}
		if(i==1) {num[0]=2;den[0]=1;}
		else if(i%3==0) { num[0]=1; den[0]=(i/3)*2;}
		else { num[0]=1;den[0]=1;}
		int k;

		for(int j=i-1;j>=1;j--) {
			if(j==1) k=2;
			else if(j%3==0) k=(j/3)*2;
			else k=1;
			copyarr(temp1, den);
			multiply(temp1, LEN, k);
			add(num, temp1, LEN);
			copyarr(temp, num);
			copyarr(num,den);
			copyarr(den, temp);
		}

		cout <<"numerator: ";
		printarr(den, LEN);
		cout <<"denominator: ";
		printarr(num,LEN);
		cout << endl;
		int s=0;
		//cout << endl<< sum(den[1]);
		for(int j=0;j<LEN;j++){
			s+=sum(den[j]);
		}
		cout << s;


	//cout << totalcnt;

	return 0;
}

