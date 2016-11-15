// combinatoric selections
#include <iostream>
#include <cmath>
using namespace std;

void factorial(int n, int arr[100])
{
	int a=0, i=1;
	while(i<=n) {arr[a]=i;a++;i++;}
}

void combination(int n, int r)
{
	int nn[100]={1};
	int rr[100]={1};
	int nr[100]={1};
	factorial(n, nn);
	factorial(r, rr);
	factorial(n-r, nr);
	for(int i=0;i<100;i++){
		if(r>n-r){
		if(nn[i]==rr[i]){ nn[i]=1; rr[i]=1;}
		}
		else {
			if(nn[i]==nr[i]){ nn[i]=1; nr[i]=1;}
		}
	}
	for(int i=0;i<100; i++)cout <<nn[i]<< " ";
	cout <<endl;
	for(int i=0;i<100; i++)cout <<nr[i]<< " "; cout <<endl;
	for(int i=0;i<100; i++)cout <<rr[i]<< " ";
}

int main()
{
	combination(23, 13);
}
