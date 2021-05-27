#include<iostream>
using namespace std;

    // CREATE 2 DIMENTIONAL ARRAY

    // datatype arrayName[rows = height][column = row]


// int height=5,width=6;



int main(){

    int m,n;


    int array[3][3]; // declaration
    int arrar_1[2][2]={1,2,3,4}; // declaration and initialization
    int array_2[2][2]={(1,1),(2,2)};

// FOR printing this array 
    for (n=0 ; n < 2 ; n++ ){
        for (m=0 ; m < 2 ; m++){
            cout << array_2[n][m];
        }

        cout << endl; // second row in next line
    }
    return 0;

}