#include<stdio.h>
// Inserting element in the array

int main(){
    int length_of_array=5;
    int second_largest,large;
    int arr[length_of_array],i=0;
    for(int i=0;i<length_of_array;i++){
        // printf("\narr[%d]=",i);
        // scanf("%d",&arr[i]);
        arr[i]=i;
    }
    for(int i=0;i<length_of_array;i++){
        printf("\narr[%d]=%d",i,arr[i]);
    }
    printf("\n");

    int position,value;
    printf("\nEnter the position of element :");
    scanf("%d",&position);
    printf("\nEnter the value of element :");
    scanf("%d",&value);

    for(int i=position;i<=length_of_array-1;i++){
        arr[i+1]=arr[i];
    }

    arr[position]=value;
    length_of_array+=1;

    printf("Printing array after the Inserting element\n");
    for(int i=0;i<length_of_array;i++){
        printf("\narr[%d]=%d",i,arr[i]);
    }
    printf("\n");
}