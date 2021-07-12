#include<iostream>

using namespace std;

class Account{

    public:
    int no;
    string name;
    static int count_;

    Account(int number,string name_){
        this->no=number;
        this->name=name_;
        count_++;
    }
    void display(){
        cout<<no<<" "<<name<<" "<<count_<<endl;
    }
    
};


int Account::count_=0;


int main(){
    Account a1 =Account(201, "Sanjay"); //creating an object of Account 
    a1.display(); 
    Account a2=Account(202, "Nakul");   
    Account a3=Account(203, "Ranjana");  
   
    a2.display();
    a3.display();

    return 0;
}