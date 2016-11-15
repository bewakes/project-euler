// powerful digit sum
#include <iostream>
using namespace std;

int sum(int n)
{
	int sum=0;
	while(n) {
		sum+=n%10;
		n/=10;
	}
	return sum;
}

int largesum(int *arr, int len) {
	int s=0;
	for(int i =0;i<len;i++)
		s+=sum(arr[i]);
	return s;
}

void multiply(int *arr, int len, int n)
{
	int rem=0;
	for(int i=0;i<len; i++) {
		int c=arr[i]*n +rem;
		arr[i]=c%100;
		rem=c/100;
	}
}

int main()
{
	int maxsum=0;

	for(int i=1;i<100; i++) {

		for(int j=1;j<100; j++) {
		int prod[200]={0};
		prod[0]=i;
			for(int k=1; k<=j;k++) {
				multiply(prod,200, i);
			}
			int sum=largesum(prod, 200);
			if(sum>maxsum){
                cout << sum<<endl;maxsum=sum;
            }
		}
	}
	cout << maxsum;

}
