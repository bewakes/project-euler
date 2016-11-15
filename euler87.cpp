#include <iostream>
#include <cmath>
#include<vector>
#include <set>
#include <cstdio>
using namespace std;

const long N = 50000000;
int total=1;
int all[N]={0};
int sqprime = int(pow(N, 0.5));
vector<long> primes;
int squares[2000] = {0};
int cubes[2000] = {0};
int fours[2000] = {0};
int cnt;

void print_vec(vector<long> v) {
    for(int i=0;i<v.size();i++) {
        cout << v[i]<<" ";
    }
    cout << endl;
}

long sq(long n) {
    return n*n;
}
long cube(long n) {
    return n*n*n;
}
long fourth(long n) { 
    return n*n*n*n;
}


void primegen()
{
	primes.push_back(2);
	int j, cnt = 1;
	for(int i=3;i<sqprime;i+=2) {
		bool flag=true;
		for(j=0; primes[j]*primes[j]<= i;j++) {
			if(i%primes[j]==0) {
                flag = false;break;
            }
		}
		if(flag){primes.push_back(i); cnt++; }
	}
	total = cnt;
}

int main()
{

	primegen();
    /*
	int sqcnt=0, cubecnt=0, fourcnt=0;
	for(int x = 0;primes[x]*primes[x]<50000000;x++) {
		squares[sqcnt] = primes[x]*primes[x];
		sqcnt++;
	}
	for(int x = 0;primes[x]*primes[x]*primes[x]<50000000;x++) {
		cubes[cubecnt] = primes[x]*primes[x]*primes[x];
		cubecnt++;
	}

	for(int x = 0;primes[x]*primes[x]*primes[x]*primes[x]<50000000;x++) {
		fours[fourcnt] = primes[x]*primes[x]*primes[x]*primes[x];
		fourcnt++;
	}
    */
	//cout << squares[929]<< " "<<cubecnt<<" "<<fourcnt<<endl;return 0;
    for(int i=0;i<primes.size();i++) {
        //if(primes[i]>=7071)break;
        long s = sq(primes[i]);
        for(int j=0;j<primes.size();j++) {
            long c = cube(primes[j]);
            //if( s+c >=N)break;
            for(int k=0;k<primes.size();k++) {
                long f= fourth(primes[k]);
                long sm = s+c+f;
                if(sm<N)
                    all[sm-1] = 1;
                else
                    break;

            }
        }
    }
    int cntall= 0;
    for(int i=3;i<N-1;i++) {
        if(all[i]==1) cntall++;
    }
    cout << cntall;
}
