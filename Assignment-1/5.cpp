#include<iostream>
#include<string>
using namespace std;
int main()
{
    int i,n=0,j;
    string str;
    cout<<"Enter string";
    cin>>str;
    for(i=0;i<str.length();i++)
    {
        int a=str[i];
        if(a<=97)
           n=a-96;
        else
            n=a-64;
        for(j=1;j<=n;j++)
        {
            if(n%2==0)
                cout<<"$";
            else
                cout<<"#";
        }
    }
    return 0;
}