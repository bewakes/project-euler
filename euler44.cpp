#include <iostream>
using namespace std;

bool inarr(long *arr, int len, long val) 
{
	for (int i=0;i<len;i++) {
		if(arr[i]==val)return true;
		if(arr[i]>val) return false;
	}
	return false;
}

int main()
{
	int n;
	int last;
	bool loop = true;
	long penta[5000] = {0}, pentnum;
	for(int i=1; i<=5000;i++)penta[i-1]=i*(3*i-1)/2;
	for(n=2;;n++) {
		if(n>1) {
			for(int i=0; i<n-1;i++) {
				if(i%1000==0)cout << i<<endl;
				if(inarr(penta, 5000, penta[i]+penta[n-1])) {
					if(inarr(penta, 5000, penta[n-1]-penta[i])){
						cout << penta[n-1] << " " << penta[i]<<endl; return 0;
					}
				}
			}
		}
	}
}
