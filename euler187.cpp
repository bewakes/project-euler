#include <iostream>
#include <cmath>
#include <vector>
using namespace std;

const int P = 50000000;

vector<bool> primes(P,true);
vector<unsigned int> prime_nos;

void sieve_primes(int n) 
{
    int sqrtn = int(sqrt(n));
    primes[0] = 0;
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
    
    for(int x=0;x<P;x++)
        if(primes[x])prime_nos.push_back(x+1);

    int count=0;
    for(int x=0;x<prime_nos.size()-1;x++)
    {
        for(int y=x;y<prime_nos.size();y++)
        {
            if(prime_nos[x]*long(prime_nos[y])>=long(100000000))break;
            count+=1;
        }
    }
    cout << count;

}
