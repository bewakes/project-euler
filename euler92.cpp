#include <iostream>
using namespace std;

int sqsum(long long n)
{
	int sum=0;
	int r, a;
	while(n!=0) {
		r = n%10;
		sum+=r*r;
		n/=10;
	}
	return sum;
}

int main()
{
	int cnt=0, temp;
	for(int i = 1; i < 10000000; i++)
	{
		temp=i;
		while(1){
			if (temp==1)break;
				if(temp==89) {
					cnt+=1;
					break;
				}
				temp=sqsum(temp);
		}
	}
	cout<< cnt;
}
