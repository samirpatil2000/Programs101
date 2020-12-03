#include<stdio.h>

int main(){
    int arr[10]={78,54,59,87,84,98,34,58,53,99};
    printf("\n");
    printf("%p %p %p \n",arr,&arr[0],&arr);

    int *ptr = &arr[0];
    
    printf("\n %d \n",*ptr);

    ptr++;

    printf(" %d \n",*ptr);


    // int *ptr
    // ptr = arr   <== similiar ==>   ptr = &arr[0]


}