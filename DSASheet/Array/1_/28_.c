#include<stdio.h>
// #define N=5;

void bruteForce(int arr[],int length){
    int max=-999;
    for(int i=0;i<length;i++){
        int product=1;
        for (int j=i;j<length;j++){
            product=product*arr[j];
            if(product>max){
                max=product;
            }
        }
    }
    printf("\nThe Max product using bruteForce %d \n",max);
}

void kadensAlgo(int arr[],int length){
    int max=-999;
    int current_prod=1;
    for (int i=0;i<length;i++){
        current_prod=current_prod*arr[i];
        if(current_prod>max){
            max=current_prod;
        }
        if(current_prod<0){
            current_prod=1;
        }
    }
    printf("\nThe Max product using kadens %d \n",max);  
}

int main(){
    int arr[]={2, 3, 4, 5, -1, 0};
    int length=sizeof(arr) / sizeof(arr[0]);
    bruteForce(arr,length);
    kadensAlgo(arr,length);
}