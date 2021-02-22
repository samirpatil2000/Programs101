#include<stdio.h>

void swap(int a,int b){
    int temp=a;
    a=b;
    b=temp;
}

void insertionSort(int arr[],int len){
    int temp=arr[0];
    int j=1;
    while(j<len && arr[j]<=temp){
        arr[j-1]=arr[j];
        j++;
    }
    arr[j-1]=temp;
}


void printArray(int arr[],int len){
    for(int i=0;i<len;i++){
        printf("%d \t",arr[i]);
    }
    printf("\n");
}


int main(){
    int arr1[]={1, 3, 5, 7};   // i
    int arr2[]={0, 2, 6, 8, 9}; // j
    int len1=sizeof(arr1)/sizeof(arr1[0]);
    int len2=sizeof(arr2)/sizeof(arr2[0]);
    int j=0,i=0;
    int count=0;
    while(1){
        i=0;
        while(i<len1 && arr2[j]>=arr1[i]){
            i++;
        }
        if(i==len1){
            break;
        }
        int temp=arr1[i];
        arr1[i]=arr2[j];
        arr2[j]=temp;
        insertionSort(arr2,len2);
        count++;
        if(count<10000){
            printf("Counter break \n");
            break;
        }
    } 

    printArray(arr1,len1);
    printArray(arr2,len2);
}