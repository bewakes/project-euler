// lychrel numbers
#include <iostream>
using namespace std;

void copyarr(int *b, int *a, int len=50) {
	for(int i=0;i<len;i++)b[i]=0;
	for(int i=0;i<len;i++) {
		b[i]=a[i];
	}
}

void add(int *arr1, int *arr2, int len=50)
{
	int rem=0;
	int c;
	for(int i=0;i<len; i++) {
		c=arr1[i]+arr2[i]+rem;
		arr1[i]=c%10;
		rem=c/10;
	}
}

void add(int *arr, int n, int len=50)
{
	int rem=0;
	int c;
	c=arr[0]+n;
	for(int i=0;i<len;i++) {
		arr[i]=c%10;
		c=c/10;
	}
}

void reversearr(int *arr, int len=50)
{
	int i=len-1, temp, l;
	while(arr[i]==0)i--;
	l=i;
	for(i=l;i>=(int)((float)l/2 + 0.5f);i--){
		temp=arr[i];
		arr[i]=arr[l-i];
		arr[l-i]=temp;
	}
}

bool isequal(int *a, int *b, int len=50)
{
	for(int i=0;i<len;i++)if(a[i]!=b[i])return false;
	return true;
}

void printarr(int *a, int len=50)
{
	for(int i=len-1;i>=0;i--)cout << a[i];
	cout <<endl;
}

bool ispalindrome(int *a, int len=50)
{
	int temp[50]={0};
	copyarr(temp, a);
	reversearr(temp);
	return isequal(a, temp);
}

int main()
{
	int lychrel=0;
	for(int i=1;i<10001;i++) {
		int temp[50]={0}, a[50]={0};
		add(a,i);
		int cnt=0;
		bool pal=false;
		while(cnt<55) {
			copyarr(temp, a);
			reversearr(temp);
			add(a, temp);
			if(ispalindrome(a)){pal=true; break;}
			cnt++;
			//cout <<cnt<<endl;
		}
		if(!pal){ cout <<i<<" is lychrel"<<endl; lychrel++; }
		else cout << i << " is not lychrel"<<endl;

	}
	//if(isequal(a, temp)) cout <<"Palindrome!!!";
	//else cout << "Not Palindrome!!!";
	cout << "*******"<<lychrel;
	return 0;
}
