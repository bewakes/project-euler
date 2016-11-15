#include <cstdio>
#include <iostream>

using namespace std;

#define fiftyMillion 50000001
#define sz 10001
#define mx 101
bool p[sz],ans[fiftyMillion+2];
long primeTable[1230],ind = 0;

void print_arr(long a[1230]) {
    for(int i=0;i<1230;i++) {
        cout << primeTable[i]<< " ";
    }
    cout << endl;
}

void sieve(){
    long i,j;

    for( i = 4; i < sz; i += 2)
        p[i] = true;
     primeTable[ind++] = 2;
    for(i = 3; i <= mx; i += 2){
        if(!p[i]){
            primeTable[ind++] = i;
            for( j = i+i; j <= sz; j += i)
                p[j] = true;
        }
    }

    for(i = mx+2; i <= sz; i += 2){
        if(!p[i])
            primeTable[ind++] = i;
    }
}

int main(){
 long i,j,k,l,cnt=0;
 long sum,S,Q,F;

 sieve();
 print_arr(primeTable);

 //printf("%ld\n",ind);

 for(i = 0;i < ind;i++){  
  S = primeTable[i] * primeTable[i];
  if(S>fiftyMillion)
   break;
  for( j = 0; j < ind; j++){   
   Q =  primeTable[j] * primeTable[j] * primeTable[j];
   if(Q+S>fiftyMillion)
    break;
   for(k = 0; k < ind; k++){
    F =  primeTable[k] * primeTable[k] * primeTable[k] * primeTable[k]; 
    if(F+Q+S>fiftyMillion)
     break;
    sum = S + Q + F;
    if(!ans[sum]){
     cnt++;
     ans[sum] = true;
    }    
   }
  }

 }
 printf("%ld\n",cnt);

 return 0;
}
