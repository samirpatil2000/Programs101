#include<iostream>
#include<string>

using namespace std;

/*  Printing this one
    1
    2 3
    4 5 6
    7 8 9 10
*/

void patternPrinting_1(int n){

    /*
           %
          %%
         %%%
        %%%%
    */

    for(int i=0;i<n;i++){
        for (int j=i;j<n;j++){
            cout<<" ";
        }
        for(int k=0;k<=i;k++){
            cout<<"%";
        }
        
        cout<<endl;
    }
    
}

void patternPrinting_2(int n){
    for(int i=0;i<n;i++){
        for (int j=i;j<n;j++){
            cout<<"#";
        }
        cout<<endl;
    }
}






int main(){
    int i,j,n=0;
    int k=1;
    cout<<"Enter the number :\n";
    // cin>>n;
    cout<<endl;


    patternPrinting_1(4);
    patternPrinting_2(4);






    for ( i=1; i <= n; i++){
        for ( j=1; j <= i; j++){
            cout<<" "<<k;
            k++;  //  you are such a dum samir ....
        }
        cout<<endl;
    }

}