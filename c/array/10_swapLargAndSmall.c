#include<stdio.h>
// swap large and small number using function 



int largeNumber(int arr[10],int n){
    int large=arr[0];
    int largeIndex=0;
    for(int i;i<n;i++){
        if(arr[i]>large){
            large=arr[i];
            largeIndex=i;
        }
    }
    return largeIndex;
}

int smallNumber(int arr[10],int n){
    int small=arr[0];
    int smallIndex=0;
    for(int i;i<n;i++){
        if(arr[i]<small){
            small=arr[i];
            smallIndex=i;
        }
    }
    return smallIndex;
}

int swap(int largeIndex,int smallIndex,int arr[10]){
    
    int large=arr[largeIndex] , small=arr[smallIndex];

    arr[largeIndex]=small;
    arr[smallIndex]=large;
}

int readArr(int arr[10],int n){
    for(int i;i<n;i++){
        printf("arr[%d]= %d\n",i,arr[i]);
    }
}

int main(){
    int n=10,min,temp;
    int arr[10]={78,54,59,87,84,98,34,58,53,99};

    printf("\nPrinting the array before swapping");
    printf("\n");
    readArr(arr,n);

    int large=largeNumber(arr,10) ,small=smallNumber(arr,10);
    swap(large,small,arr);


    printf("\nPrinting the array after Swaping the array");
    printf("\n");
    readArr(arr,n);



}