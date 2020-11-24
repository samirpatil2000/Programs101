#include<stdio.h>
# define N 4

int main(){
    int arr[N],n,i;
    printf("Enter the number :\n");
    
    for(i=0;i<N;i++){
        scanf("%d",&n);
        arr[i]=n;
    }

    printf("Printing the array :\n");
    // printf(arr);

    for (i=0;i<N;i++){
        printf("%d\n",arr[i]);
    }
}