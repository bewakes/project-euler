#include <iostream>
#include <cmath> 
#include <vector>
using namespace std;

void find_continued(long n)
{
    long sqr = long(sqrt(n));

    if (sqr==sqrt(n)){
        cout <<"no convergents";
        return;
    }
    cout << sqr<<" "; // which is a0;
    long count = 0;
    long d = 1,dn;
    long a = sqr;
    long r = sqr, rn;
    long p1,p2,q1,q2,p,q;
    p = a;
    q = 1;
    p1=1;
    q1=0;
    while(1)
    {
        dn = n-r*r;
        if(dn%d!=0)cout<<"error..";
        //cout << "d "<< dn<<" ";
        dn/=d;
        //cout << "d "<< dn<<" ";
        a = (sqr+r)/dn;
        p2 = p;
        q2 = q;
        p = a*p+p1;
        q = a*q+q1;
        p1 = p2;
        q1 = q2;
        cout << "p "<<p<<" q "<<q<<endl;
        //if(a==2*sqr)break;
        //cout <<" a "<< a<<" ";
        r = dn*a-r;
        //cout << " r "<<r<<endl;
        d = dn;
        count+=1;
        if(count==25)break;
    }
}

int main()
{
    cout << "start..";
    find_continued(2);
}
