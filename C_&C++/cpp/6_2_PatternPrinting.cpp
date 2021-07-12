#include<iostream>
#include<string>

using namespace std;

/*  Printing this one
   
*/

int main(){
    int i,j,n;
    cout<<"Enter the number :\n";
    cin>>n;
    cout<<endl;

    for ( i=1; i <= n; i++){
        for ( j=1; j<=i; j++){
            cout<<" # ";
        }
        cout<<endl;
    }
     for ( i=1; i <= n-1; i++){
        for ( j=i ; j <= n-1 ; j--){
            cout<<" # ";
        }
        cout<<endl;
    }

}