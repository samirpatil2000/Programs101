#include<stdio.h>
int main(){
    int i=0,avg,n,sum;
    printf("Enter the number\n");
    scanf("%d",&n);
    do
    {
       
        sum=sum+i;
        i=i+1;

    } while (i <= n);
    avg=(float)sum/n;
    
    printf("The average is %d and sum is %d\n",avg,sum);

}