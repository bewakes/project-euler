#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
using namespace std;

const int P = 10000000;

vector<bool> primes(P,true);
vector<unsigned int> prime_nos;
vector<unsigned int> phis(P,0);

void sieve_primes(int n) 
{
    int sqrtn = int(sqrt(n));
    primes[0]=0;
    int count = 2;
    for(count=2;count<sqrtn;)
    {
        for(int i=count;;i++)
        {
            if (count*i>P)break;
            primes[count*i-1] = 0;
        }
        //print_sieve();
        while(primes[count]!=1)count++;
        count+=1;
        //cout << "\nbroken\n"<< count;
        if(count== sqrtn) break;
    }
}

int len(int n)
{
    int cnt=0;
    while(n!=0)
    {
        cnt+=1;
        n/=10;
    }
}

bool is_perm(int a, int b)
{
    if(len(a)!=len(b))return false;
    vector<int>aa,bb;
    while(a!=0)
    {
        aa.push_back(a%10);
        bb.push_back(b%10);
        a/=10;
        b/=10;
    }
    sort( aa.begin(), aa.end());
    sort( bb.begin(), bb.end());
    for(int x=0;x<aa.size();x++)
        if(aa[x]!=bb[x])return false;
    return true;
}

int gcd(int a, int b)
{
    int r = a%b;
    while(r!=0)
    {
        a = b;
        b = r;
        r = a%b;
    }
    return b;
}

int main()
{
    double min = 9999999;
    int number = 2;
    sieve_primes(P);
    for(int i=0;i<P;i++)
        if(primes[i])prime_nos.push_back(i+1);
    
    phis[0] = 1; // phi for 1 is 1
    int temp, m;
    int sqr,p;
    for(int i=2;i<P;i++)
    {
        if(!(i&1))// if even
        {
            m =  i>>1;
            if(!(m&1))
            {
                temp =2*phis[m-1];
                //cout << i<< " "<<2*phis[m-1]<<endl;
            }
            else
            {
                temp = phis[m-1];
                //cout << i<< " "<<phis[m-1]<<endl;
            }
        }
        else 
        {
            temp = i; 
            sqr = int(sqrt(i))+1;
            if(primes[i-1])
            {
                temp = i-1;
            }
            else
            for(int j=0;prime_nos[j]<=sqr;j++)
            {
                p = prime_nos[j];
                if(i%p==0)
                {
                    int gc = gcd(i/p, p);
                    temp = phis[p-1]*phis[i/p-1]* gc / phis[gc-1];
                    break;
                }
            }
        }
        phis[i-1]=temp;
        if(is_perm(i, temp))
        if(double(i)/temp<min)
        {
            number = i;
            min = double(i)/temp;
        }
    }
    cout << number <<" "<<min;
}
