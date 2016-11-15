#include <iostream>
#include <cmath>
#include <vector>
using namespace std;

int area = 1;
int diff = 1000000000;
int len, bre;

int no_rect(int l, int b)
{
    int cnt=0;
    for(int i=1;i<=l;i++)
    {
        for(int j=1;j<=b;j++)
        {
            cnt+=(j*i);
        }
    }
    return cnt;
}
int main()
{
    int l, b;
    int rects, ar;
    int d;
    for(int a = 2;a<300;a++)
    {
        for(int b=2;b<300;b++)
        {
            ar = a*b;
            rects = no_rect(a,b);
            d = abs(rects-2000000);
            if(d< diff)
            {
                diff=d;
                area = ar;
                len=a;
                bre=b;
            }
        }
    }
    cout << diff<< "  "<<ar<<endl;;
    cout << "len "<<len<<" bre "<< bre;
    return 0;
}
