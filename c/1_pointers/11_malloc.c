#include<stdio.h>
#include<stdlib.h>


int main(){
    int n;
    printf("Enter the count : ");
    scanf("%d\n",&n);

    int *ptr = (int *)malloc(n*sizeof(n));

    if (ptr == NULL){
        printf("Memory not available ");
        exit(1);
    }
    for(int i=0;i<n;i++){
        printf("Enter the number : ");
        scanf("%d",ptr+i);
    }
    for(int i=0;i<n;i++){
        printf("%d",*(ptr+i));
    }

}