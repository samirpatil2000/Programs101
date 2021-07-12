#include<iostream>
#include<string>

using namespace std;

int addingArray(int array[]){
    int result,n;
    for (n=0 ; n<5 ; n++){
        result+=array[n];
    }
    cout <<"The addition of the array is " << result <<"\n";
}

int main(){
    // FOR ARRAY
    //type name [elements];
    // int array[5];
    int array[] = { 16, 2, 77, 40, 12071 };   
    int a = array[2];  // access to an element of the array.
    cout<< a <<"\n";  

// calling the addition func
    addingArray(array);

    return 0;
}

