#include<iostream>

using namespace std;

class Car{
    public:
        string brand;
        int year;

};

int main(){
    Car carObject1;
    carObject1.brand="BMW";
    carObject1.year=2020;
    
    cout << carObject1.brand << " " << carObject1.year << "\n";
}