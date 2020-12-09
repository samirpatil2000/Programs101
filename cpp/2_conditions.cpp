#include<iostream>
using namespace std;

int main(){
    // condition ? result1 : result2

    int a,b,c;
    cout<<"Enter the value of a ,b \n:";
    cin >> a;
    cin >> b;
    c=(a>b) ? a:b;
    cout<<"  "<<c <<"is  greater "<<endl;

}