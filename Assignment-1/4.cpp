#include<iostream>
#include<string>
using namespace std;
string encrypt(string s)
{
    int i;
    char c;
    string str;
    for(i=0;i<s.length();i++)
    {
        if(isupper(s[i]))
          str=str+char(int(s[i]+5-65)%26+65);
        else
            str=str+char(int(s[i]+5-97)%26+97);
    }
    return str;
}
string decrypt(string s)
{
    int i;
    char c;
    string str;
    for(i=0;i<s.length();i++)
    {
        if(isupper(s[i]))
          str=str+char(int(s[i]-5-65)%26+65);
        else
            str=str+char(int(s[i]-5-97)%26+97);
    }
    return str;
}
int main()
{
    int ch;
    string st;
    cout<<"Enter 1 for encrypting\n 2 or decrypting";
    cin>>ch;
    cout<<"Enter string";
    cin>>st;
    if(ch==1)
        cout<<"Encrypted string: "<<encrypt(st);
    else
        cout<<"Decrypted string: "<<decrypt(st);
    return 0;
}