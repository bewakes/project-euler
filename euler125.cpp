// quite inefficient, I should have used formula

#include <iostream>
#include <cmath>
using namespace std;

bool isPalindrome(int n)
{
	int k=n; int sum=0;
	while(n) {
		sum=sum*10+n%10;
		n=n/10;
	}
	return sum==k;
}

bool asSum(int i) {
	if(i==1) return false;
	int temp = sqrt(i)/pow(2,0.5)+0.5;
	int j;
	int sum;
	bool flag;
	while(temp>0) {
		sum = i;
		j=temp;
		flag=false;
		while(sum>0) {
			sum-=(j*j);
			if(sum==0) { return true; }
			j-=1;
			if(j<1) break;
		}
		temp--;
	}
	return false;
}

int main()
{
	int count; long total = 0;
	for(int i=1;i<100000000;i++) {
		if(isPalindrome(i)) {
			if(asSum(i)) { total+=i; }			
		}
	}
	cout << endl << total << endl;
	return 0;
}