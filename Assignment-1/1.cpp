#include<iostream>
#include<cstdlib>
using namespace std;
int main(int arc, char *arv[])
{
    cout<<"Numbers Entered: "<<arc-1<<"\n";
    int num[arc-1];
    int i;
    for(i=1;i<arc;i++)
        num[i-1]=atoi(arv[i]);
    int small=num[0];
    for(i=1;i<arc-1;i++)
    {
        if(num[i]==small)
        {
            cout<<"Entered 2 same numbers. Enter different numbers\n";
            exit(0);
        }
        else if(num[i]<small)
            small=num[i];
    }
    cout<<"Smallest number: "<<small<<endl;
    return 0;
}
