// prime digit replacements
#include <iostream>
#include <cmath>
#include "primegen.cpp"
using namespace std;

int sieve[1000000] = {1};
int prime_nos[1000000]={0};
int total_primes=0;

void copyarr(int *b, int *a, int len=50) {
	for(int i=0;i<len;i++)b[i]=0;
	for(int i=0;i<len;i++) {
		b[i]=a[i];
	}
}

void printarr(int *a, int len=50)
{
	for(int i=len-1;i>=0;i--)cout << a[i];
	cout <<endl;
}

void add(int *arr1, int *arr2, int len=50)
{
	int rem=0;
	int c;
	for(int i=0;i<len; i++) {
		c=arr1[i]+arr2[i]+rem;
		arr1[i]=c%10;
		rem=c/10;
	}
}

void add(int *arr, int n, int len=50)
{
	int rem=0;
	int c;
	c=arr[0]+n;
	for(int i=0;i<len;i++) {
		arr[i]=c%10;
		c=c/10;
	}
}

int getval(int *arr, int len=50)
{
	int val=0;
	for(int i=len-1;i>=0;i--) {
		val=val*10+arr[i];
	}
	return val;
}

bool inarr(int *arr, int val, int len)
{
	int high, low;
	high=len-1;
	low=0;
	int avg=(high+low)/2;
	while(1) {
		if(val==arr[avg])return true;
		if((avg==high or avg==low) and val!=arr[avg])return false;
		if(val<arr[avg]) {
			high=avg;
		}
		else low=avg;
		avg=(high+low)/2;
	}
}

int on(int x) // gives the total number of 1s in the binary representations
{
	int cnt=0;
	for(int i=0;i<6;i++) {
		if((x&(1<<i)))cnt++;
	}
	return cnt;
}

bool checkreplace(int n, int r)	// n is the number to check and r is the total digits to be replaced
{
	if(r>(int)log10(n))return false;
	int num[50]={0},temp1[50]={0};
	add(num, n);int store[8];
	for(int x=0;x<(2<<((int)(log10(n))-1));x++)
	{
		if(on(x)==r){
			int cnt=0;
			copyarr(temp1, num);
			//cout << endl;
			for(int j=0;j<10;j++) {
				for(int i=0;i<5;i++) {
					if((x&(1<<i)))temp1[i+1]=j;
				}
				//if(inarr(primes,getval(temp1), total)){if(getval(temp1)>=n)cnt++; store[cnt-1]=getval(temp1);}
				if(sieve[getval(temp1)-1]){if(getval(temp1)>=n)cnt++; store[cnt-1]=getval(temp1);}
				if(cnt==8){ cout << store[0];return true; }
			}
		}
	}
	return false;
}


void print_sieve()
{
    cout << "sieve : ";
    for(int i=0;i<10;i++)
        cout << sieve[i]<< " ";
        cout <<endl;
}

void sieve_primes() // only 1000000
{
    sieve[0] = 0;
    int count = 2;
    for(count=2;count<1000;)
    {
        for(int i=count;;i++)
        {
            if (count*i>1000000)break;
            sieve[count*i-1] = 0;
        }
        //print_sieve();
        while(sieve[count]!=1)count++;
        count+=1;
        //cout << "\nbroken\n"<< count;
        if(count== 1000) break;
    }
}

void get_repitition(int n, int digit, int *pos)
{
    for(int i=0;i<6;i++)pos[i]=0;
    int count=0;
    while(n!=0)
    {
        if(n%10==digit) { 
            pos[5-count]=1;
        }
        count+=1;
        n/=10;
    }
}

bool substitute(int n, int *pos)
{
    int k = n;
    int count=0;
    for(int i=1;i<10;i++)
    {
        bool flag=false;
        for(int j=5;j>=0;j--)
        {
            if(pos[j]==1){
                flag=true;
                int first = n/int(pow(10, 6-j));
                int last = n%int(pow(10, 6-j-1));
                n = (first*10+i)*int(pow(10,6-j-1))+last;
                //cout << "first"<< first<<" last "<<last<<endl;;
            }
        }
        //cout << "  substituted n: "<< n<<endl;

        if(flag && sieve[n-1]){ count+=1;}
    }
    if(count==8)
    {
        return true;
    }
    return false;
}

bool check(int n)
{
    int pos[6]={0,0,0,0,0,0};
    for(int i=0;i<10;i++)
    {
        get_repitition(n,i,pos);
        if(substitute(n, pos))return true;
    }
    return false;
}

int main()
{
    for(int i=0;i<1000000;i++)sieve[i]=1;
    sieve_primes();

    for(int i=2;i<1000000;i++) {
        if(sieve[i-1])
        {
            prime_nos[total_primes]=i;
            total_primes++;
        }
    }

    for(int i=0;i<total_primes;i++)
    {
        if(check(prime_nos[i]))
        {
            cout << "found ";
            cout << prime_nos[i]<<endl;
            return 0;
        }
    }

	int i;
	for(i=2;i<1000000;i++) {
		//cout <<primes[i]<< "*******";
        if(sieve[i-1])
		for(int k=1;k<6;k++)
		{
			if(checkreplace(i, k)){ return 0;}
		}
	}
}

