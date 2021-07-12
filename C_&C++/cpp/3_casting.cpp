#include<iostream>
using namespace std;
int main(){
    int i;
    float j=3.14;
    i=j;
    cout<< i << "\n";   // i=3
    i=int(j);
    cout<< i <<"\n"; //i=3
    cout<< "The size of i is "<<sizeof(i) <<"\n"; //i=3

    // for loops

    int x;
    cout<<"Enter the number \n:";
    cin>>x;
    while(x>0){
        cout<<x<<",";
        x--;
    }






}