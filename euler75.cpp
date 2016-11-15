#include <iostream>
#include <vector>
using namespace std;

const int perimeter = 1500000;
vector<int> perims(perimeter, 0);// count of perimeter

vector< vector<int> > triplets;
void generate_triplets(int a, int b, int c)
{
    int a1=a-2*b+2*c, b1= 2*a-b+2*c, c1=2*a-2*b+3*c;
    int a2 = a+2*b+2*c, b2 = 2*a+b+2*c, c2 = 2*a+2*b+3*c;
    int a3 = -a+2*b+2*c, b3=-2*a+b+2*c, c3 = -2*a+2*b+3*c;
    vector<int> temp(3,0);
    if(a1+b1+c1<=perimeter)
    {
        temp[0]=a1;temp[1]=b1;temp[2]=c1;
        triplets.push_back(temp);
        generate_triplets(a1,b1,c1);
    }
    if(a2+b2+c2<=perimeter)
    {
        temp[0]=a2;temp[1]=b2;temp[2]=c2;
        triplets.push_back(temp);
        generate_triplets(a2,b2,c2);
    }
    if(a3+b3+c3<=perimeter)
    {
        temp[0]=a3;temp[1]=b3;temp[2]=c3;
        triplets.push_back(temp);
        generate_triplets(a3,b3,c3);
    }

}

int perim(vector<int>a)
{
    return a[0]+a[1]+a[2];
}

int main()
{
    int a=3,b=4,c=5;
    vector<int> temp(3);
    temp[0]=3;temp[1]=4;temp[2]=5;
    triplets.push_back(temp);

    generate_triplets(a,b,c);

    int cnt =0;
    for(int x=0;x<triplets.size();x++)
    {
        int prim_peri = perim(triplets[x]);
        for(int y=1;y*prim_peri<perimeter;y++)
        {
            perims[y*prim_peri-1]+=1;
        }
    }
    for(int x=0;x<perimeter;x++)
    {
        if(perims[x]==1)cnt+=1;
    }
    cout<< cnt;
}
