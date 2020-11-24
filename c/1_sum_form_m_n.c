#include<stdio.h>

int main(){

    int n,m,i=0,sum,a,b;
    printf("Enter the number ");
    scanf("%d%d",&n,&m);
    if (m>n){
        b=m;
        a=n;
        i=a;
    }
    else
    {
        b=n;
        a=m;
        i=a;
    }
    while (i < b){
        i=i+1;
        sum=sum+i;   
    }
    printf("The sum is %d",sum);

}