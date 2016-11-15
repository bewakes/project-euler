#include <iostream>
#include <fstream>

bool check(int* sudoku, int index);

bool solve(int* sudoku)
{
    for(int i=0;i<81;i++)
        if(sudoku[i]==0)
            goto notcomplete;
    return true;

    notcomplete:
       for(int i=0;i<81;i++)
       {
           if(sudoku[i]==0)
           {
               for(int j=1;j<10;j++)
               {
                   sudoku[i] = j;
                   // check for validity
                   if(check(sudoku,i))
                   {
                       if(solve(sudoku))
                           return true;
                   }
               }
               sudoku[i] = 0;
               return false;
           }
       }
}

bool check(int* sudoku, int index)
{
    int val = sudoku[index];

    // check in the row
    int start = (index/9)*9;
    for(int i=start;i<start+9;i++)
        if(i!=index and sudoku[i]==val)
            return false;

    // check in the column
    start = index%9;
    for(int i=start;i<81;i+=9)
        if(i!=index and sudoku[i]==val)
            return false;

    // check in the box
    int cnt =0;
    for(start=(index/27)*27;cnt<27;start++)// bounding
    {
        cnt++;
        if((start%9)/3 == (index%9)/3) // in the bound, so check
        {
            if(sudoku[start] == val and start!=index )
                return false;
        }
    }
    return true;
}

int main()
{
    std::ifstream f("sudoku.txt");
    std::string s;
    getline(f,s);// first line
    int count =0;
    int index=0;
    int sudoku[81];
    while(getline(f,s))
    {
        std::cout << s<<std::endl;;
        for(int k=0;k<s.length();k++)
        {
            sudoku[index]=s[k]-'0';
            index++;
        }
        count+=1;
        if(count>8)break;
    }
    for (int i=0;i<81;i++)
        std::cout << sudoku[i] << " ";
    std::cout << "\n";
    solve(sudoku);
    for (int i=0;i<81;i++)
    {
        std::cout << sudoku[i] << " ";
        if((i+1)%9==0)std::cout << "\n";
    }
    return 0;
}
