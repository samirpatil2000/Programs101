#include<iostream>
#include<string>

using namespace std;
/*  Printing this one 

     $
    $$$
   $$$$$
  $$$$$$$
 $$$$$$$$$

*/

int main(){
    int n;
    cout<<"Enter the number :\n";
    cin>>n;
    cout<<endl;
    for (int i=1,k=0;i<=n;i++,k=0){
        for (int j=0 , k=0 ;j<=(n-i);j++,k=0){
            cout<<" ";
        }
        while(k != (2*i-1)){
            cout<<"$";
            k++;
        }
        cout<<endl;
    }
}
