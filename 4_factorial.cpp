#include<iostream>
#include<string>

using namespace std;

long factorials(int n){
    if (n > 1){
        return(n*factorials(n-1));
    }
    else{
        return(1);   
    }
}

int main(){
    int num;
    cout << "Enter the number \n:";
    cin >> num;
    cout << factorials(num)<<"\n";
}