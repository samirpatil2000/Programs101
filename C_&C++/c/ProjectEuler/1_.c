#include<stdio.h>

long fib(long n){
    if (n==1){
        return 0;
    }

    else if (n==2){
        return 1;
    }
    else{
        return fib(n-1)+fib(n-2);
    }
}  

int main(){
    printf("%ld\n",fib(5));
    long i=2;
    long sum;
    // int arr[];
    while (i<20){
        long num=fib(i);
        if (num%2==0){
            sum=sum+num;
            printf("%ld",i);
            i=i+1;
        }
        printf("%ld",i);
        // i=+1;

    }
    printf(" the sum is %ld\n",sum);
    // printf("%d\n",fib(5));
}