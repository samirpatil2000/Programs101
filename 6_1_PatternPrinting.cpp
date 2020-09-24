#include<iostream>
#include<string>

using namespace std;

/*  Printing this one
    1
    2 3
    4 5 6
    7 8 9 10
*/

int main(){
    int i,j,n;
    int k=1;
    cout<<"Enter the number :\n";
    cin>>n;
    cout<<endl;

    for ( i=1; i <= n; i++){
        for ( j=1; j <= i; j++){
            cout<<" "<<k;
            k++;  //  you are such a dum samir ....
        }
        cout<<endl;
    }

}