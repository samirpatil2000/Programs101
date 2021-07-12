#include<iostream>

using namespace std;

// find largest number amoung three
int main(){
    int num1,num2,num3;
    cout<<"Enter three numbers one by one "<<endl;
    cin>>num1;
    cin>>num2;
    cin>>num3;
    if (num1>=num2 && num1>=num3){
        cout<<num1<<" Is greater among three"<<endl;
    }
    else if  (num2>=num1 && num2>=num1){
        cout<<num2<<" Is greater among three "<<endl;
    }
    else{
        cout<<num3<<" Is greater among three"<<endl;
    }
    return 0;
}