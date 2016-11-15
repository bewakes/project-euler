// poker hands
#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;

char order[13]={'2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A'};
unsigned int royal_flus=10, straight_flus=9, four_kind=8, full_house=7, flus=6, straight=5, three_kind=4, two_pairs=3, one_pair=2, highcard=1;

int getindex(char x, char * arr, int len=13)
{
	for(int i=0;i<len;i++) if(arr[i]==x)return i;
	return -1;
}

class Hand
{
private:
	char cards[5][3];
	bool ROYAL, STRAIGHT_FLUS, FOUR, FULL, FLUS, STRAIGHT, THREE, TWO_PAIRS, PAIR, HIGH;
	char three;
	char cpair;
	char highpair;
	char four;
public:
	Hand() {
		ROYAL=false; STRAIGHT_FLUS=false; FOUR= false; FULL=false; FLUS=false;
		STRAIGHT=false; THREE=false; TWO_PAIRS=false; PAIR= false; HIGH=false;
		three='*';
		cpair='*';
		highpair='*';
		four='*';
	}
	void set_data(char *a);
	void sort_data();
	void find_rank();
	bool compare_rank(Hand h); // returns true if rank of the calling object is higher
	void display() { for(int i=0;i<5;i++)cout << cards[i]<< endl; }
	int _rank;
};

void Hand::set_data(char a[50])
{
	int cnt = 0;
	int index = 0;
	int temp=0;
	while(cnt!=5) {
		cards[index][0] = a[temp];
		cards[index][1] = a[++temp];
		cards[index][2] = '\0';
		temp+=2;
		cnt+=1;
		index+=1;
	}
	sort_data();
}

void Hand::sort_data()
{
	char temp[3];
	for(int i=0; i<4;i++){
		for(int j=i+1;j<5;j++) {
			if(getindex(cards[i][0], order)>getindex(cards[j][0], order)) {
				strcpy(temp, cards[j]);
				strcpy(cards[j], cards[i]);
				strcpy(cards[i], temp);
			}
		}
	}
}

void Hand::find_rank()
{
	// check for flus
	FLUS=true;
	for(int i=0; i<4;i++){
		if(cards[i][1]!=cards[i+1][1]){ FLUS=false; break;}
	}
	// check for royal flus
	if(FLUS) {
		if(cards[0][0]=='T' && cards[1][0]=='J' && cards[2][0]=='Q' && cards[3][0]=='K' && cards[4][0]=='A') { _rank = royal_flus; ROYAL=true; return; }
	}
	// check for straight/straight_flus
	STRAIGHT=true;
	for(int i=0;i<4;i++) {
		if(getindex(cards[i][0], order)!= getindex(cards[i+1][0], order)-1) {STRAIGHT=false; break; }
	}
	if(STRAIGHT and FLUS ) { _rank=straight_flus; return; return; }
	if(FLUS) { _rank=flus; return;}
	if(STRAIGHT) { _rank=straight; return;}

	// check for four of a kind
	if((*cards[0]==*cards[1] && *cards[0]==*cards[2] && *cards[0]==*cards[3] && *cards[0]==*cards[0]) or
	   (*cards[4]==*cards[1] && *cards[4]==*cards[2] && *cards[4]==*cards[3] && *cards[4]==*cards[4])) { _rank = four_kind; four = cards[2][0];return; }

	// check for three of a kind
	int cnt=0;
	for(int i=0;i<3;i++) {
		if(cards[i][0]==cards[i+1][0] and cards[i][0]==cards[i+2][0]) { THREE=true; three=cards[i][0];}
	}

	// check for pair
	int paircount=0;
	for(int i=0;i<4;i++) {
		if(cards[i][0]==cards[i+1][0] and cards[i][0]!= three and cards[i][0]!=cpair){ paircount++; if(paircount==2) highpair=cards[i][0];
		if(paircount==1)cpair=cards[i][0];}
	}

	if(paircount==1 and THREE) { _rank=full_house; return; }
	if(THREE) { _rank=three_kind; return; }
	if(paircount==2) { _rank=two_pairs; return;}
	if(paircount==1) { _rank= one_pair; return;}

	_rank=highcard;
	return;
}

bool Hand::compare_rank(Hand h2)
{
	if(_rank>h2._rank) return true;
	if(_rank<h2._rank) return false;
	if(_rank==h2._rank) {
			// if straight flush or straight
			if(_rank==straight_flus or _rank==straight) {
				return getindex(cards[4][0], order) > getindex(h2.cards[4][0], order);
			}
			// if four of a kind
			if(_rank==four_kind){
				int p1=getindex(four, order), p2=getindex(h2.four, order);
				if(p1>p2) return true;
				if(p1<p2) return false;
				if(p1==p2) {
					return getindex(cards[4][0], order)> getindex(h2.cards[4][0], order);
				}
			}
			// if full house
			if(_rank==full_house) {
				int p1=getindex(three, order), p2=getindex(h2.three, order);
				if(p1>p2) return true;
				if(p1<p2) return false;
				if(p1==p2) {
					p1=0;p2=0;
					for(int i=0;i<5;i++) {
						p1+= getindex(cards[i][0], order);
						p2+= getindex(h2.cards[i][0], order);
					}
					return p1>p2;
				}
			}
			// if three of a kind
			if(_rank==three_kind) {
				int p1=getindex(three, order), p2=getindex(h2.three, order);
				if(p1>p2) return true;
				if(p1<p2) return false;
				if(p1==p2) {
					for(int i=4;i>=0;i--) {
						if(getindex(cards[i][0], order)>getindex(h2.cards[i][0], order)) return true;
						if(getindex(cards[i][0], order)<getindex(h2.cards[i][0], order)) return false;
					}
					return p1>p2;
				}
			}
			// if single pair
			if(_rank==one_pair) {
				int p1=getindex(cpair, order), p2=getindex(h2.cpair, order);
				if(p1>p2) return true;
				if(p1<p2) return false;
				if(p1==p2) {
					for(int i=4;i>=0;i--) {
						if(getindex(cards[i][0], order)>getindex(h2.cards[i][0], order)) return true;
						if(getindex(cards[i][0], order)<getindex(h2.cards[i][0], order)) return false;
					}
					return p1>p2;
				}
			}
			// if double pair
			if(_rank==two_pairs) {
			int p1=getindex(highpair, order), p2=getindex(h2.highpair, order);
			if(p1>p2) return true;
				if(p1<p2) return false;
				if(p1==p2) {
					for(int i=4;i>=0;i--) {
						if(getindex(cards[i][0], order)>getindex(h2.cards[i][0], order)) return true;
						if(getindex(cards[i][0], order)<getindex(h2.cards[i][0], order)) return false;
					}
					return p1>p2;
				}
			}
			// if flush or high card
			if(_rank==flus or _rank==highcard) {
				for(int i=4;i>=0;i--) {
						if(getindex(cards[i][0], order)>getindex(h2.cards[i][0], order)) return true;
						if(getindex(cards[i][0], order)<getindex(h2.cards[i][0], order)) return false;
					}
			}
	}
}

int main()
{
	FILE * fp;
	int total=0;
	fp=fopen("poker.txt", "r");
	char temp[50],temp1[50];
	char c=fgetc(fp);
	while(c!=EOF) {
		int cnt=0;
		while(c!='\n') {
			temp[cnt++]=c;
			c=fgetc(fp);
	}
	int i;
	for(i=0;i<15;i++) temp1[i]=temp[i];
	Hand h1, h2;
	h1.set_data(temp1);
	h2.set_data(temp+i);
	h1.find_rank();
	h2.find_rank();
	if(h1.compare_rank(h2)) total++;
	c=fgetc(fp);
	}
	fclose(fp);
	cout << total;
	return 0;
}
