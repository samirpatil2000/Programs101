#include<stdio.h>


int* mergeTwoArray(int arr1[],int arr2[],int n1,int n2){
    int num=n1+n2;
    int new_arr[num];
    int i=0,j=0,k=0;
    // new_arr[]={};
    while (i<=n1 && j<=n2)
    {
        if(arr1[i]>arr2[j]){
            new_arr[k]=arr2[j];
            j++;
        }else if(arr1[i]<arr2[j]){
            new_arr[k]=arr1[i];
            i++;
        }else{
            new_arr[k]=arr1[i];
            k++;
            new_arr[k]=arr2[j];
            i++;j++;
        }
        k++;
    }
    if(i>n1){
        while (j<=n2)
        {
            new_arr[k]=arr2[j];
            j++;k++;
        }
    }
    if(j>n1){
        while (i<=n1)
        {
            new_arr[k]=arr1[i];
            i++;k++;
        }
    }
    
}

void printArray(int arr[],int n){
    printf("\n");
    for (int i = 0; i < n; i++)
    {
        printf("\t %d",arr[i]);
    }
    printf("\n");
}

int main(){
    int n1 = 6, A[] = {1, 5, 10, 20, 40, 80};
    int n2 = 5, B[] = {6, 7, 20, 80, 100};
    int n3 = 8, C[] = {3, 4, 15, 20, 30, 70, 80, 120};
    // printArray(C,n3);   
    int* new_arr=mergeTwoArray(A,B,n1-1,n2-1);
    printArray(new_arr,(n1-1)+(n2-1));
}