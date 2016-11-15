#include <iostream>
#include <vector>
using namespace std;

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

vector<int> between(vector<int>a, vector<int>b)
{
    int aa = a[0]+b[0],
        bb = a[1]+b[1];
    vector<int> ret(2,0);
    int gc = gcd(aa,bb);
    ret[0] = aa/gc;
    ret[1] = bb/gc;
    return ret;
}

int main()
{
    int cnt =0;
    int d = 12000;
    vector< vector<int> > current;
    vector<int> start,end,mid;
    start.push_back(1);start.push_back(3);
    end.push_back(1);end.push_back(2);
    current.push_back(start);
    current.push_back(end);

    while(current.size()!=0)
    {
        end = current[current.size()-1];
        current.pop_back();
        start = current[current.size()-1];
        current.pop_back();
        mid = between(start, end);
        if(mid[1]<=d)
        {
            cnt+=1;
            current.push_back(start);
            current.push_back(mid);
            current.push_back(mid);
            current.push_back(end);
        }
    }
    cout << cnt;
}
