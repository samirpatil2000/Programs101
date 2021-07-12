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


// is prime or not

bool isPrime(int n){
    if (n%2==0){
        return false;
    }else{
        for (int i=3;i<n;i++){
            if(n%i==0){
                return false;
            }
        }
    }
    return true;
    
}

int main(){
    int num;
    cout << "Enter the number \n:";
    cin >> num;
    // cout << factorials(num)<<"\n";
    string prime=(isPrime(num)==1)? "Prime":"Not Prime";
    cout<<num<<" is "<<prime<<endl;
}


