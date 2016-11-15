#include <iostream>
#include <vector>
using namespace std;

const int P = 362880*9;
vector<int> table(P,0);

int fam169[] = {169, 363601, 1454};
int fam871[] = {871,45361};
int fam872[] = {872, 45362};

int in169(int n)
{
    if(n==169)return 0;
    if(n==363601)return 1;
    if(n==1454) return 2;
    return -1;
}

int in871(int n)
{
    if(n==871)return 0;
    if(n==45361) return 1;
    return -1;
}

int in872(int n)
{
    if(n==872)return 0;
    if(n==45362) return 1;
    return -1;
}

int factorials[] = {1,1,2,6,24,120,720,5040,40320,362880};

int fac_sum(int n)
{
    int s = 0;
    while(n!=0)
    {
        int r = n%10;
        s+=factorials[r];
        n/=10;
    }
    return s;
}

int calc_terms(int n)
{
    int count = 1;
    int s=n;
    int temp;
    while (true)
    {
        temp = fac_sum(s);
        if(temp==s)return count; 
        s = temp;
        if(table[s-1]!=0)
        {
            table[n-1] = count+table[s-1];
            return count+table[s-1];
        }
        int a = in169(s);
        if(a!=-1)
        {
            table[n-1] = count + a+1;
            return table[n-1];
        }
        a = in871(s);
        if(a!=-1)
        {
            table[n-1] = count + a+1;
            return table[n-1];
        }
        a = in872(a);
        if(a!=-1)
        {
            table[n-1] = count + a+1;
            return table[n-1];
        }
        count+=1;
    }
}

int main()
{
    table[168] = 3;
    table[870] = 2;
    table[871] = 2;

    int count=0;
    for(int i=1;i<1000000;i++)
    {
        if(calc_terms(i)>=61)count+=1;
    }
    cout << count;

}
