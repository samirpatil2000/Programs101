#include<iostream>
#include<stdlib.h>

using namespace std;


int randint(int Min, int Max) {
    return std::rand() % (Max + 1 - Min) + Min;
}

int main(){
    // This program will create same sequence of 
    // random numbers on every program run 
    int start=1,end=90;






    // int Number = std::rand() % (Max + 1 - Min) + Min;

    int outPut = rand()%((end - start) + 1) + start; 
 
    // for(int i = 0; i<5; i++){
    //     cout<<rand()<<endl;
    // } 
    // cout<<Number<<endl;
    // cout<<outPut<<endl;


    for(int i=23;i<30;i++){
        cout<<randint(0,23)<<endl;
    }
    return 0;
}