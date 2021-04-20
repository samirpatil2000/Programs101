#include<stdio.h>

/*
Given five positive integers, find the minimum and maximum values that can be calculated by 
summing exactly four of the five integers. 
Then print the respective minimum and maximum values as a single line of two space-separated long integers.
Example 
arr=[1,3,5,7,9]
The minimum sum is 1+3+5+7 =16
and 
the maximum sum is 3+5+7+9 =24
.The function prints
16 24
*/

int min_max_sum(int arr[5]){
    long min=arr[0],max=arr[0];
    long max_sum=0,min_sum=0;
    for(int i=0;i<5;i++){
        if(arr[i]>max){
            max=arr[i];
        }
        if(arr[i]<min){
            min=arr[i];
        }
    }
    printf("%ld %ld\n",max,min);
    if(min == max ){
        for(int i=1;i<5;i++){
            max_sum+=arr[i];
        }
        min_sum=max_sum;
    }
    else
    {
        for (int i=0;i<5;i++){

        if(arr[i] != max){
            max_sum+=arr[i];
        }
        if(arr[i] != min){
            min_sum+=arr[i];
        }
        }
    }
    
    printf("%ld %ld\n",max_sum,min_sum);
}


int main(){
    // unsorted array
   int arr[5]={5, 5, 5, 5, 5};
   
   min_max_sum(arr);


}