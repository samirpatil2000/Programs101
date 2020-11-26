#include<stdio.h>
// Inserting element in the sorted array


// void insertElement(int length_of_array,int position,int value,int arr[]){

//     for(int i=length_of_array-1;i>=position;i--){
//         arr[i+1]=arr[i];
//     }

//     arr[position]=value;
//     length_of_array+=1;

//     printf("Printing array after the Inserting element\n");
//     for(int i=0;i<length_of_array;i++){
//         printf("\narr[%d]=%d",i,arr[i]);
//     }
//     printf("\n");

// }

int main(){
    int length_of_array=5;
    int second_largest,large;
    int arr[length_of_array],i=0;
    for(int i=0;i<length_of_array;i++){
        printf("\narr[%d]=",i);
        scanf("\n%d",&arr[i]);
        // arr[i]=i;
    }
    for(int i=0;i<length_of_array;i++){
        printf("\narr[%d]=%d",i,arr[i]);
    }
    printf("\n");

    int position,value;
    // printf("\nEnter the position of element :");
    // scanf("%d",&position);
    printf("\nEnter the value of element :");
    scanf("%d",&value);

    for (int i=0;i<length_of_array;i++){

        if (value<arr[i]){
            for (int j = length_of_array-1; j>=i; j--){
                 arr[j+1]=arr[j]; 
                           
            }
            arr[i]=value;
            break;
        }
    }
    
    length_of_array+=1;

    printf("Printing array after the Inserting element\n");
    for(int i=0;i<length_of_array;i++){
        printf("\narr[%d]=%d",i,arr[i]);
    }
    printf("\n");



}