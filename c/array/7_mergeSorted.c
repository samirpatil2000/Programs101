#include<stdio.h>
#define N1 10 
#define N2 14

// merge SORTED array

int main(){
    
    int arr1[N1]={34,36,57,67,69,70,75,77,79,84};
    int arr2[N2]={35,45,66,67,89,90,95,107,179,184,189,203,234,355};
    //int arr2[N2]={35,45,66,67,89,90,95,107,179,234};

    int array[N1+N2]={0};

    printf("\nPrinting the array 1");
    printf("\n");
    for(int i=0;i<N1;i++){
        printf("arr[%d]= %d\n",i,arr1[i]);
    }

    printf("\nPrinting the array 2");
    printf("\n");

    for(int i=0;i<N2;i++){
        printf("arr[%d]= %d\n",i,arr2[i]);
    }

    int length_of_arr1=0,length_of_arr2=0,index=0; 
    while (length_of_arr1 <N1 && length_of_arr2<N2 )
    {
        if(arr1[length_of_arr1]>arr2[length_of_arr2]){
            array[index]=arr2[length_of_arr2];
            length_of_arr2++; index++;
        }
        else if (arr1[length_of_arr1]<arr2[length_of_arr2])
        {
            array[index]=arr1[length_of_arr1];
            length_of_arr1++; index++;
        }
        else
        {
            array[index]=arr1[length_of_arr1];
            array[index+1]=arr2[length_of_arr2];
            index+=2; length_of_arr1++; length_of_arr2++;
        }
        
    }


    if(length_of_arr1<N1){
        for(int i=length_of_arr1;i<N1;i++){
            array[index]=arr1[i];
            index++;
        }
    }
    else{
        for(int i=length_of_arr2;i<N2;i++){
            array[index]=arr2[i];
            index++;
        }
    }
    

    
    printf("\nPrinting the merge array");
    printf("\n");

    for(int i=0;i<N1+N2;i++){
        printf("arr[%d]= %d\n",i,array[i]);
    }





}