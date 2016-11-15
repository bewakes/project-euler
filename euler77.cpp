#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

const int N = 1000000;
vector<int> primes = {2};

vector<int>prime_hash(N, 1);

void print_arr(vector<int>arr) {
    for(int i=0;i<arr.size();i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

void sieve() {
    for(int i=2; i*i<=N; ) {
        for(int j=2;i*j<=N;j++) {
            prime_hash[i*j-1] = 0;
        }
        i+=1;
        while(prime_hash[i-1]==0) i++;
    }
}

void generatePrimes(int n) {
    int start = 3;
    bool prime;
    while(1) {
        prime= true;
        for(int i=0; primes[i]*primes[i]<=start;i++) {
            if(start % primes[i]==0) {
                prime=false;
                break;
            }
        }
        if(prime) primes.push_back(start);
        start++;
        if(start>n)break;
    }
}

vector<int> c_vals;
vector<int> b_vals;

int c(int n) {
    int s = 0;
    for(int i=2;i<=n;i++) {
        if(n%i==0)
            s+= prime_hash[i-1]* i;
    }
    return s;
}

int b(int n) {
    int s;
    s = c(n);
    c_vals.push_back(s);
    for(int i=1;i<n;i++) {
        s+= c_vals[i-1]*b_vals[n-i-1];
    }
    return s/n;
}

int main() {
    sieve();

    b_vals.push_back(0);
    c_vals.push_back(0);

    int b_val;
    for(int i=2;;i++) {
        b_val = b(i); 
        b_vals.push_back(b_val);
        if(b_val>5000){ cout << i; break;}
    }
}
