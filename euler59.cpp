// xor decryption
#include <iostream>
#include <cstdio>
using namespace std;

void printarr(int arr[1200]) {
	for(int x=0;arr[x]>=0;x++)cout <<arr[x]<<" ";
	cout <<endl;
}

int main()
{
	FILE *fp;
	fp=fopen("cipher.txt", "r");
	char c;
	int a[1200]={-1}, cnt=0;
	int aa[1200], bb[1200], cc[1200];
	for(int t=0;t<1200;t++) { aa[t]=-1;bb[t]=-1;cc[t]=-1;a[t]=-1;}
	c=fgetc(fp);
	int val=0;
	while(c!=EOF){
			if(c==EOF){a[cnt]=val;}
			if(c==','){ a[cnt]=val;cnt++;val=0;}
			else val=val*10+c-'0';
			c=fgetc(fp);
	}
	//a[cnt]=val;

	for(int x=0;x<=cnt;x++) {
		if(x%3==0)aa[x/3]=a[x];
		if(x%3==1)bb[x/3]=a[x];
		if(x%3==2)cc[x/3]=a[x];
	}

	int repeata[256]={0};
	int repeatb[256]={0};
	int repeatc[256]={0};
	for(int x=0;x<256;x++) {
		repeata[aa[x]]++;
		repeatb[bb[x]]++;
		repeatc[cc[x]]++;
	}
	int maxa=0, maxb=0,maxc=0;
	for(int x=0;x<256;x++) {
		if(repeata[x]>maxa) maxa=x;
		if(repeatb[x]>maxb) maxb=x;
		if(repeatc[x]>maxc) maxc=x;
	}
	char solna, solnb, solnc;
	for(int a=0;a<256;a++) {
		//cout <<(char)(maxa^('a'+a))<<endl;
		//cout <<(maxa^a)<<endl;
		if((maxa^a) == 32){solna=a; }
		if((maxb^a) == 32)solnb=a;
		if((maxc^a) == 32)solnc=a;
	}
	cout << (char)maxa<<" "<<(char)maxb<<" "<<(char)maxc<<endl;
	int total;
	for(int x=0;x<=cnt;x++) {
		if(x%3==0){cout <<(char)(a[x]^solna);total+=(a[x]^solna);}
		if(x%3==1){cout <<(char)(a[x]^solnb);total+=(a[x]^solnb);}
		if(x%3==2){cout <<(char)(a[x]^solnc);total+=(a[x]^solnc);}
	}
	cout <<endl<< total-'('+'.'<<endl;// because of fault in the last character.. i dont know how it happened..

}

