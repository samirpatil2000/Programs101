#include<stdio.h>
// We have to count summed of even numbers from fibbonacci
// max number 4000000

// 1 1 2 3 5 8 13 21 34 55 89 144 ... 
// a b c a b c  a  b  c  a  b  c 

int fib(int n){
    int a,b,sum,c;
    a=0;
    b=1;
    if (n==1){
        return 0;
    }
    else{
        for(int i=1;i<n;i++){
            c=a+b;
            a=b;
            b=c;
        }
        return c;
    }
}

int main(){
    int a=1 ,b=1,c=a+b;
    int sum=0;
    while(sum<4000000){
        
        // if (c%2==0){
        //     sum+=c;
        // }
        
        a=b+c;
        b=c+a;
        c=a+b;
        sum+=c;
    }
    printf("%d\n",sum);
    // int n=6;
    // printf("The number is %d\n",fib(n));

}