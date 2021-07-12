#include<stdio.h>
#include<math.h>
//The prime factors of 13195 are 5, 7, 13 and 29.
//What is the largest prime factor of the number 600851475143 ?

int prime_factors(long n){
    int arr[100],index;
    int sq=(int) sqrt(n);
    for(long i=0;i< sq+1;i++){
        if (n%i==0){
            arr[index++]=i;
        }
    }
    return arr;
}


int main(){
    // int number=600851475143;
    int number=17;
    int arr=prime_factors(number);

    // consider array length
    int arr_length=100;
    printf("%d",arr);

    
    // for (int i=0;i<arr_length;i);
}