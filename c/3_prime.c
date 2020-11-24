#include <stdio.h>
// #include <conio.h>
int main(){

    int flag = 0 ,i,n;
    printf("Enter the number\n");
    scanf("%d",&n);

    for (i=0; i<n/2; i++){
        if (n%i == 0){
            flag=1;
            break;
        }
    }
    if (flag==1){
        printf("The %d is composite number ",n);
    }
    else{
        printf("The %d is prime number ",n);
    }

    return 0;
}