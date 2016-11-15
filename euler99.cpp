#include <iostream>
#include <cstdio>
#include <cmath>
using namespace std;

int arr[1000][2];

int main()
{
	// file portion
	FILE *fp;
	fp=fopen("base_exp.txt", "r");
	int cnt=0;
	while(fscanf(fp,"%d,%d\n",&arr[cnt][0],&arr[cnt][1])!=EOF){
		cnt++;
	}

	int maxline=1;
	int maxbase=arr[0][0];
	double maxpower=arr[0][1];
	int base;
	double power;
	double factor;
	for(int x=1;x<1000;x++) {
		base=arr[x][0];
		power=arr[x][1];
		factor=(float)(log(base)/log(maxbase));
		if(factor*power>maxpower) {
			maxbase=base;
			maxpower=power;
			maxline=x+1;
		}
	}
	cout << maxline<<endl;
}
