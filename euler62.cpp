// cubic permutations
#include <iostream>
#include <cmath>
using namespace std;

void bubblesort(int *arr, int len)
{
	int a, b, temp;
	for(a=0;a<len-1;a++) {
		for(b=a+1;b<len;b++) {
			if(arr[a]>arr[b]) {
				temp=arr[a];
				arr[a]=arr[b];
				arr[b]=temp;
			}
		}
	}
}

int isPermutation(long a, long b) {
	if((int)log10(a)!=(int)log10(b)) return -1;
	int c=(int)log10(a) + 1;
	int *aa=new int[c];
	int *bb=new int[c];
	for(int i=1;i<=c;i++) {
		aa[i-1]=a%10;
		a=a/10;
		bb[i-1]=b%10;
		b=b/10;
	}
	bubblesort(aa,c);
	bubblesort(bb,c);
	for(int i=0;i<c;i++)if(aa[i]!=bb[i])return 0;
	return 1;

}

int main()
{
	int n;
	long c,d;
	int cnt, t;
	for(n=345;;n++) {
		c=n*n*n;
		cnt=0;
		for(t=n+1;;t++) {
			d=t*t*t;
			int k=isPermutation(c,d);
			if(k==1) {cnt++;}
			if(k==-1)break;
			if(cnt==3)break;
		}
		if(cnt==3)break;
	}
}
