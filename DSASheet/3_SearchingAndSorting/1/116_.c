#include<stdio.h>
#define MAX 100

int productOfArr(int arr[],int len){
    int product=1;
    for(int i=0;i<len;i++){
        product=product*arr[i];
    }
    return product;
}

void printArray(int arr[],int len){
    for(int i=0;i<len;i++){
        printf("%d \t",arr[i]);
    }
    printf("\n");
}

int main(){
    int arr[]={10, 3, 5, 6, 2};   // i
    int len=sizeof(arr)/sizeof(arr[0]);
    int productArr[MAX]={};
    

    int product=productOfArr(arr,len);
    for(int i=0;i<len;i++){
        int current_product=product/arr[i];
        productArr[i]=current_product;
    }
    printArray(arr,len);
    printArray(productArr,len);


}