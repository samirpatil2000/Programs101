#include<stdio.h>

/*
candles=[4,4,1,3]
The maximum height candles are 4 units high. There are 2 of them, so return 2
*/

int max_num(int arr[5]){
    int max=arr[0];
    int counter=0;
    for(int i=0;i<5;i++){
        if(arr[i]>max){
            max=arr[i];
        }
    }
    for(int i=0;i<5;i++){
        if(arr[i]==max){
            counter+=1;
        }
    }
    printf("%d\n",counter);
}


int main(){
    // unsorted array
   int arr[5]={5, 5, 2, 3, 1};
   
   max_num(arr);


}