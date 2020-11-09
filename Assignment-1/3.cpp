#include<iostream>
#include<cmath>
using namespace std;
int main()
{
    int i,r1,r2,c=0;
    cout<<"Enter starting point\n";
    cin>>r1;
    cout<<"Enter ending point\n";
    cin>>r2;
    if(r1>r2)
    {
        cout<<"Enter valid range";
        return 0;
    }
    for(i=r1;i<=r2;i++)
    {
        for(int j=2;j<(int)sqrt(i);j++)
        {
            if(i%j==0)
            {
                c=1;
                break;
            }
        }
        if(c==0)
            cout<<i<<",";
        c=0;
        return 0;
    }

}