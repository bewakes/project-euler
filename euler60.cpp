#include <iostream>
#include <cmath>
#include <vector>
using namespace std;

const int P = 100000000;

vector<bool> primes(P,true);
vector<unsigned int> prime_nos;

vector< vector <unsigned int> > fours;


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

int len(int n)
{
    int count  = 0;
    while(n!=0)
    {
        count+=1;
        n/=10;
    }
    return count;
}

bool isconcat_prime(int a, int b)
{
    int p1 = a*int(pow(10, len(b))) + b;
    int p2 = b*int(pow(10, len(a))) + a;
    return primes[p1-1] && primes[p2-1];
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

int sz = 5;
vector< unsigned int> curr_vec;

void generate_fours(int index)
{

    for(int i=index;prime_nos[i]<9999;i++)
    {
        if(curr_vec.size()==0){
            curr_vec.push_back(prime_nos[i]);
            generate_fours(i+1);
        }
        else if(curr_vec.size()==sz)
        {
            for(int j=0;j<sz;j++)cout<<curr_vec[j]<<" ";
            cout << endl;
            fours.push_back(curr_vec);
            curr_vec.pop_back();
            return;
        }
        else
        {
            bool flag=false;
            for(int j=0;j<curr_vec.size();j++)
            {
                if(! isconcat_prime(prime_nos[i], curr_vec[j]))
                {
                    flag=true;
                    break;
                }
            }
            if (!flag)
            {
                curr_vec.push_back(prime_nos[i]);
                generate_fours(i+1);
            }

        }
    }
    curr_vec.pop_back();
}


int main()
{
    sieve_primes(P);
    
    for(int i=0;i<P;i++)
        if (primes[i]) prime_nos.push_back(i+1);
    cout << "primes generated\nnow fives...\n";

    generate_fours(0);
}
