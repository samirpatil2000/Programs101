#include<iostream>

using namespace std;

int countBinary(int n){
    int prevZero=1;
    int prevOne=1;
    for (int i=2;i<n;i++){
        int tempOnes=prevOne;

        prevOne=prevZero+prevOne;
        prevZero=tempOnes;

    }
    return prevOne+prevZero;
}

int main(){
    cout<<countBinary(6)<<endl;
}