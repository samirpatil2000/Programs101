#include<iostream>
#include<string>

using namespace std;

// In C++ two different functions can have the same name 
//if their parameter types or parameter number are different

int operate(int x,int y){
    return(x*y);
}
float operate(float x, float y){
    return(x/y);
}

int main(){
    cout<<"\n --- OVERLOADING --- " << "\n";
    int a=5,b=4;
    float v=9,f=3;
    cout << operate(a,b)<<"\n";
    cout<< operate(v,f)<<"\n" ;
}

