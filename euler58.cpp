#include <iostream>
#include <cmath>
#include <vector>
using namespace std;

const int P = 10000000;

vector<bool> primes(P,true);
vector<unsigned int> prime_nos;

void print(unsigned int n)
{
    cout << "printing..\n";
    for(int x=0;x<32;x++)
    {
        cout << (n&(0x80>>x!=0)) << " ";
    }
    cout << endl;
}

/*
void set(long n, int val=0)
{
   int index = n/(32);
   int offset = n%(32);
   if(val==0)
       primes[index] &= ~(0x8000>>n);
    else
        primes[index] |= (0x8000>>n);
}

int get(int n)
{
    int index = n/(32);
    int offset = n%(32);
    return (primes[index] & (0x8000 >> n))!=0;
}
*/

bool isprime(long n)
{
    int sqr = int(sqrt(n));
    for(int x=0;;x++)
    {
        if(n%prime_nos[x]==0)return false;
        if(prime_nos[x] > sqr)break;
    }
    return true;
}

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


int main()
{
    sieve_primes(P);
    for(int i=0;i<P;i++)
        if (primes[i]) prime_nos.push_back(i+1);

    int total_diags = 1;
    long d1, d2,d3,d4;
    int prime_cnt = 0;
    for(int i=2;;i++)
    {
        total_diags+=4;
        d1 = 4* i*i - 10*i+7;
        d2 = 4*i*i - 8*i+5;
        d3 = 4*i*i - 6*i+3;
        cout << "d1 "<< d1 <<" d2 "<< d2<<" d3 "<<d3<<endl;

        if(d1<P)
        {
            if(primes[d1-1]) prime_cnt+=1;
        }
        else
        {
            if(isprime(d1)) prime_cnt+=1;
        }

        if(d2<P)
        {
            if(primes[d2-1]) prime_cnt+=1;
        }
        else 
        {
            if(isprime(d2)) prime_cnt+=1;
        }

        if(d3<P)
        {
            if(primes[d3-1]) prime_cnt+=1;
        }
        else
        {
            if(isprime(d3)) prime_cnt+=1;
        }


        if (100*prime_cnt < 10*total_diags){ cout << i*2-1;break;}
    }
}
