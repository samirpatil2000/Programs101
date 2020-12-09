#include <iostream>

using namespace std;

int main()
{
    char c;
    int counter=0;
    int number=0;
   cout << "Hello World" << endl; 
   do{
       counter=counter+1;
       cout<<" counter "<< counter <<"\n Previous number "<< number <<endl;
       cin>>number;
       cout<<"To continue press c"<<"\n";
       cin>>c;
   }while(c=='c');
   return 0;
}