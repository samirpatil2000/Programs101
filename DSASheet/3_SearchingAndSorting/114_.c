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
        while(i<len1){
            if(arr2[j]>=arr1[i]){
                i++;
                printf("i==%d\n",i);
            }else{
                swap(arr1[i],arr2[j]);
                insertionSort(arr2,len2);
                i=0;
            }
        }
        printf("i==%d\n",i);
        if(i==len1){
            break;
        }
        count++;
        if(count<10000){
            printf("Counter break \n");
            break;
        }
    } 

    printArray(arr1,len1);
    printArray(arr2,len2);
}