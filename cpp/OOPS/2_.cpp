#include<iostream>

using namespace std;

class Student{
    private:
        string name;
        int phy,chem,maths;

    public:
        void setDetails(string user_name,int phy_marks,int math_marks,int chem_marks){
            name=user_name;
            phy=phy_marks;
            chem=chem_marks;
            maths=math_marks;
        }
    public:
        double getDetails(void){
            // this function for printing the details
            cout<<"Name : "<<name<<endl;
            int avg=(phy+chem+maths)/3;
            cout<<"Avg : "<<avg<<endl;
        }
};


int main(){
    Student student_1;
    student_1.setDetails("Madhumita",90,98,78);
    cout<<student_1.getDetails();
    return 0;
}