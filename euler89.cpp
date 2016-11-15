#include <iostream>
#include <cstdio>
using namespace std;

string roman[]={"I","IV", "V","IX", "X","XL", "L", "XC", "C", "CD", "D", "CM", "M"};
int values[]={1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000};

string convert(int n)
{
	string a="";
	int i,j,k;
	while(n) {
		for(i=0;i<13;i++) {
			if(values[i]>n) {a+=roman[i-1]; n-=values[i-1];break;}
			if(i==12 and values[i]<=n){ a+=roman[i]; n-=values[i];break;}
		}
	}
	return a;
}

int getindex(string a, string arr[])
{
	for(int x=0;x<13;x++) {
		if(a==arr[x])return x;
	}
	return -1;
}

int read(string a)
{
	char temp[2];
	char temp1[2];
	int val=0;
	for(int x=0;x<a.length();x++) {
		temp[0]=a[x];temp[1]='\0';
		temp1[0]=a[x-1];temp1[1]='\0';
		int c=values[getindex(temp, roman)];
		int d=values[getindex(temp1, roman)];
		val+=c;
		if(x>0 and d<c) {
			val-=2*d;
		}
	}
	return val;
}

int main()
{
	//cout << read("XL");return 0;
	FILE *fp;
	fp=fopen("roman.txt", "r");
	string a[1000];
	char temp[50];
	int cnt=0;
	while(fscanf(fp,"%s\n",temp)!=EOF) {
		a[cnt]=temp;
		cnt++;
	}
	int total=0;
	for(int x=0;x<1000;x++) {
		cout << a[x]<< "                    "<< read(a[x]) <<"              "<< convert(read(a[x]))<<endl;

		int c=a[x].length();
		string tt=convert(read(a[x]));
		total+=(c-tt.length());
	}
	cout << total;
}
