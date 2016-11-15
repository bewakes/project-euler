#include <iostream>
#define max 100000
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
	long a;
	a=(long)400000*(3*400000-1)/2;
	cout << a<<endl<<endl;
	long penta[max], tri[max], hexa[max];
	for (int i=1; i<=max;i++){
		penta[i-1]=(long)i*(3*i-1)/2;
		hexa[i-1]=(long)i*(2*i-1);
		tri[i-1]=(long)i*(i+1)/2;
	}
	int cnt=0;
	for(int i=0;i<max;i++){
		long c=tri[i];
		if(inarr(penta, max, c)){
			if(inarr(hexa, max, c)) {cnt++; if(cnt==3){cout << c<< endl;return 0;}}
		}
	}
}