#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

bool last2first2(int a, int b)
{
    //cout << a << " "<< b<<endl;
    bool res = (a%100==b/100 and a%100>10);
    //if(res)cout <<"okay!!\n";
	return res;
}

int solvequad(int a, int b, int c) {
    if(b*b < 4*a*c) return 0;
    float x = (-b + pow(b*b - 4*a*c, 0.5))/(2*a);
    return ceil(x);
}

void print_arr(vector<int> a) {
    for(int i=0;i<a.size();i++) 
        cout << a[i]<< " ";
    cout << endl;
}



int n_of(int poly, int num) {
    if(poly==3)
        return solvequad(1,1,-2*num);
    else if (poly==4)
        return solvequad(1,0,-num);
    else if (poly==5)
        return solvequad(3, -1, -2*num);
    else if (poly==6)
        return solvequad(2, -1, -num);
    else if (poly==7)
        return solvequad(5, -3, -2*num);
    else if (poly==8)
        return solvequad(3, -2, -num);
    else return -1;
}

vector<int> curr_list;
int lastnum = 0;
bool done=false;



int find_num(int poly, int n) {
    if(poly==3)
        return n*(n+1)/2;
    else if (poly==4)
        return n*n;
    else if (poly==5)
        return n*(3*n-1)/2;
    else if (poly==6)
        return n*(2*n - 1);
    else if (poly==7)
        return n*(5*n-3)/2;
    else if (poly==8)
        return n*(3*n-2);
    else return -1;

}

bool inarr(int n, vector<int> arr) {
    for(int i=0;i<arr.size();i++) {
        if(arr[i]==n) return true;
    }
    return false;
}

vector<int> g_poly = {3,4,5,6,7,8};

vector<int> curr;
vector<int>curr_poly;

void find_soln(int a);


void check_and_continue(int next, int polynum, int n) {
    if( last2first2 (curr[curr.size()-1], polynum) ) {

            curr.push_back(polynum);
            curr_poly.push_back(g_poly[next]);
            
            find_soln( next);
            if(curr.size()==6) {
                if(last2first2(curr[5], curr[0])) return;
            }
            curr.pop_back();
            curr_poly.pop_back();
        }
}

int count = 0;

void find_soln( int poly) {
    for(int i=1;i<=5;i++) {
        int next = (poly+i)%6;
        if(next==0 || inarr(g_poly[next], curr_poly)) {
            continue;
        }

        int n = n_of(g_poly[next], curr[curr.size()-1]%100 * 100);
        if(n<=0) continue;

        int polynum = find_num(g_poly[next],n);
        check_and_continue(next, polynum, n);
        if(curr.size()==6)return;
        
        polynum = find_num(g_poly[next], n+1);
        check_and_continue(next, polynum, n);
        if(curr.size()==6)return;

        polynum = find_num(g_poly[next], n+2);
        check_and_continue(next, polynum, n);
        if(curr.size()==6)return;

    }
}



int main()
{
    vector<int> triangles;
    //int start = n_of(3, 1000);
    for(int start =0;start<=500;start++) {
        int val = start*(start+1)/2;
        if(val>=10000 || val <1000)continue;
        triangles.push_back(val);
    }

    
    vector<int> soln;
    curr_poly.push_back(g_poly[0]);
    for(int i=0;i<triangles.size();i++) {
        curr.push_back(triangles[i]);
        find_soln(0); // g_poly[0] represents current polygon
        if(curr.size()!=6)
            curr.pop_back();
        else {
            print_arr(curr);
            return 0;
            curr.pop_back();
            curr.pop_back();
            curr.pop_back();
            curr.pop_back();
            curr.pop_back();
            curr.pop_back();
        }
    }
    return 0;
}

