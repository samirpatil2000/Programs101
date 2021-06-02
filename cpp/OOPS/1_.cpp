#include<iostream>

using namespace std;
class Student{
    public:
    int id;
    string name;

    Student(int i,string nam){
        id=i;
        name=nam;

    }

    void insert(int i,string s){
        id=i;
        name=s;
    }
    void display(){
        cout<<id<<name<<endl;
    }
};

int main(){
    Student sam=Student(22,"Sam");
    sam.id=21;
    sam.name="Samir";
    cout<<sam.id<<" "<<sam.name<<endl;
    // Student s1;
    // s1.insert(22,"Madhumita");
    // s1.display();
}