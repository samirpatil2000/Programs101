#include<iostream>
using namespace std;


void passingByValuePointer(int a){
    a+=1;
}

void passingByReferencePointer(int *a){
    *a+=1;
}

int main(){
    int a=10;
    int* aptr=&a;
    // cout<<*aptr<<endl;
    // *aptr+=10;
    // cout<<*aptr<<endl;
    passingByValuePointer(a);
    cout<<a<<endl;
    passingByReferencePointer(aptr);
    cout<<a<<endl;
}