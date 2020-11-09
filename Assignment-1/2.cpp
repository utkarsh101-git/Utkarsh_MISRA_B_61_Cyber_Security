#include<iostream>>
#include<string>
using namespace std;
int main()
{
    int i,flag=1;
    string st;
    cout<<"Enter a String";
    cin>>st;
    int j=st.length()-1;
    for(i=0;i<st.length()/2;i++,j--)
    {
        if(st[i]!=st[j])
        {
            flag=0;
            break;
        }
    }
    if(flag==0)
        cout<<"String is not palindrome";
    else
    cout<<"String is palindrome";
    return 0;
}