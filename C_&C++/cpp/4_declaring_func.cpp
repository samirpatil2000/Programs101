#include<iostream>
#include<string>

using namespace std;

void even(int n);
void odd(int n);

int main(){
     int i;


     while(i != 0){
          cout<<"Enter the number (Type '0' to exit):  ";
          cin>>i;
          odd(i);
     }
    return 0;
}
void even(int n){
    if((n%2)==0){
         cout<< n <<" is even \n";
    }
    else
    {
         odd(n);
    }
    
}

void odd(int n){
    if ((n%2)!= 0){
         cout<< n <<" is odd \n";
    }
    else{
         even(n);
    }
}