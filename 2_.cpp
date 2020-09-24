#include <iostream>

using namespace std;

int main()
{
    char c;
    int counter=0;
   cout << "Hello World" << endl; 
   do{
       counter=counter+1;
       cout<<" this is you"<< counter <<"Enter the number \n"<< endl;
       cin>>c;
   }while(c=='c');
   return 0;
}