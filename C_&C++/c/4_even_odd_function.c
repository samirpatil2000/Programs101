#include<stdio.h>

int evenodd(int a){
    if (a%2==0){
        return 1;
    }
    else{
        return 0;
    }
}

int main(){
    int num,flag;
    printf("Enter the number:");
    scanf("%d",&num);
    flag= evenodd(num);
    if (flag==1){
        printf("%d is even\n",num);
    }else{
        printf("%d is odd\n",num);
    }
}
