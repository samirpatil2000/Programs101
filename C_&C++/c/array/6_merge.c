#include<stdio.h>
#define N1 10 
#define N2 14

// merge unsorted array

int main(){
    
    int arr1[N1]={78,54,59,87,84,98,34,58,53,99};
    int arr2[N2]={58,44,52,97,94,88,36,59,43,39,89,90,30,21};

    int arr[N1+N2]={0};

    printf("\nPrinting the array 1");
    printf("\n");
    for(int i=0;i<N1;i++){
        printf("arr[%d]= %d\n",i,arr1[i]);
    }

    printf("\nPrinting the array 2");
    printf("\n");

    for(int i=0;i<N2;i++){
        printf("arr[%d]= %d  ",i,arr2[i]);
    }

    for(int i=0;i<N1;i++){
        arr[i]=arr1[i];
    }
    for(int j=N1;j<N1+N2;j++){
        arr[j]=arr2[j-N1];
    }

    /*
        Or SIMPLY

        int index=0;

        for(int i=0;i<N1;i++){
            arr[index]=arr1[i];
            index++;
        }
        for(int i=0;i<N2;i++){
            arr[index]=arr2[i];
            index++;
        }
    */

    printf("\nPrinting the merge array");
    printf("\n");

    for(int i=0;i<N1+N2;i++){
        printf("arr[%d]= %d\n",i,arr[i]);
    }






}