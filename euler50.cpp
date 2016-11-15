// consecutive prime sum

#include <iostream>
#include <cmath>
using namespace std;

int primes[500000]={0};
int total;

void primegen()
{
	primes[0]=2;
	int cnt=1;
	for(int i=3; i<=1000000; i+=2){
		bool flag=true;
		for(int j=0; primes[j]<=(int)sqrt(i)+1 and primes[j]!=0;j++){
			if(i%primes[j]==0){
				flag=false;
				break;
			}
		}
		if(flag==true){primes[cnt]=i;
		cnt++;
	}
	}
	::total=cnt;
}

bool inarr(int *arr, int len, int val)
{
	for (int i=0;i<len;i++) {
		if(arr[i]==val)return true;
		if(arr[i]>val) return false;
	}
	return false;
}

int main()
{
	primegen();
	int *counts = new int[::total];
	int index;
	int flag=1;
	int maxcnt=2;
	for (int i=total-1; i>0; i--) {

		for(int j=0; primes[j]<=primes[i]/maxcnt; j++) {

			int sum=0, temp=j, cnt=0;

			while(1) {
				if(sum>primes[i]){break;}


				sum+=primes[temp++];
				cnt++;

				if(sum==primes[i]){
					if(cnt>maxcnt) {
						maxcnt=cnt;
						index=i;
					}
					break;
					flag=0;
				}
			}
			if(flag==0)break;
		}
	}
	cout << endl<<primes[index];
	cout << endl<< maxcnt<<endl;
}
