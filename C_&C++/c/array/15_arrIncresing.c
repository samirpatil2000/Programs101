#include<stdio.h>


int printArray(int arr[20],int n){
    printf("\n");
    for (int i=0;i<n;i++){
        printf("\t %d",arr[i]);
    }
    printf("\n");
}


int main(){
    int arr[10]={0};
    printArray(arr,10);

    for(int i=1;i<10;i++){
        arr[9+i]=0;
    }

    printArray(arr,19);

    int arr_2[3]={0};
    for (int i=3;i<9;i++){
        arr[i]=0;
    }

    int size=5,i;
    int ar[size];
    for(i=0;i<size;i++)
    {
        ar[i]=0;
    }
    // printArray(arr_2,10);
    printArray(ar,size);

}