#include<stdio.h>


int fastPower(int a,int b){
    int res=1;

    while(b>0){
        if(b%2 != 0){
            res=res*a;
        }
        a=a*a;
        b=b/2;
    }
    return res;
}


int main(){
    printf("%d\n",fastPower(3,4));
}

