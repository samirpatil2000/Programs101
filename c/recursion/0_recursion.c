#include<stdio.h>
#include<math.h>
// Solve this using recursion  a**b


int power(int a,int b){
    if (b==0){
        return 1;
    }
    return a*power(a,b-1);
}

long fastPower(int a,int b){
    if(b==0){
        return 1;
    }
    else{
        if(b%2==0){
            return fastPower(a*a,b/2);
        }
        return a*fastPower(a,(b-1));
    }
}

// finding the path
int path(int m,int n){
    if (n==1 || m==1){
        return 1;
    }
    return path(n,m-1)+path(n-1,m);
}

int main(){
    int b=3;
    printf("%d\n",power(3,10000));
    printf("%ld\n",fastPower(3,10000));
    
    printf("Number of path %d\n",path(40,10));
}