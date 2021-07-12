#include<stdio.h>

int bestExample(int arr[5]){
    int *ptr1,*ptr2;
    ptr1=arr;
    ptr2=&arr[8];

    printf("%d\n",*ptr1);
    printf("%d\n",*ptr2);

    printf("\nptr2-ptr1 : %ld\n",ptr2-ptr1);

}


int main(){
    
    int arr[10]={1,2,3,4,5,6,7,8,9};

    int *ptr1,*ptr2;


    ptr1=arr;
    ptr2=arr+2;


    printf("\nptr1 %p\n",ptr1);

    printf("ptr2 %p\n",ptr2);


    printf("\nptr2-ptr1 : %ld\n",ptr2-ptr1);

    printf("\n");
    
    bestExample(arr);

}