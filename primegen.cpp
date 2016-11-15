#include <cmath>
int primes[50000000]={0};
int total=0;


void primegen(int n)
{
	primes[0]=2;
	total=1;
	int cnt=1;
	for(int i=3; i<=n; i+=2){
		bool flag=true;
		for(int j=0; primes[j]<=(int)sqrt(i)+1 and primes[j]!=0;j++){
			if(i%primes[j]==0){
				flag=false;
				break;
			}
		}
		if(flag==true){
			primes[cnt]=i;
			cnt++;
			total++;
		}
	}
}
