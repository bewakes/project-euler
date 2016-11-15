#include <iostream>
#include <cmath>
using namespace std;

void bubblesort(int *a, int len)
{
	for(int i=0;i<len-1; i++) {
		for(int j=i+1; j<len; j++) {
			if(a[i]>a[j]) {
				int temp=a[i];
				a[i]=a[j];
				a[j]=temp;
			}
		}
	}
}

bool samedigits(long a, long b)
{
	int i = (int)log10(a) + 1;
	if((int)log10(a)!=(int)log10(b)) return false;
	int aa[i], bb[i], cnt=0;
	for(cnt=0;cnt<i;cnt++) {
		aa[cnt]=a%10;
		a=a/10;
		bb[cnt]=b%10;
		b=b/10;
	}
	bubblesort(aa, i);
	bubblesort(bb, i);
	for(cnt=0;cnt<i; cnt++) {
		if(aa[cnt]!=bb[cnt]) return false;
	}
	return true;
}

int main()
{
	for(int i=1; ;i++) {
		int c = (int)pow(10, i);
		for(int j=c; j<c+(int)pow(10, i-1)*7; j++) {
			if(samedigits(j, j*2)){
				if(samedigits(j, j*3)) {
					if(samedigits(j, j*4)){
						if(samedigits(j, j*5)){
							if(samedigits(j, j*6)){
								cout << j;
								return 0;
							}
						}
					}
				}
			}
		}
	}
}
