#include<stdio.h>
# define N 10

int main(){

    int arr[N],n,i;
    int repeatedNumber[N]={0};
    
    for(i=0;i<N;i++){
        printf("Enter the number :");
        scanf("%d",&arr[i]);
    }

    printf("Printing the array :\n");

    for(i=0;i<N;i++){
        printf("\narr[%d]=%d",i,arr[i]);
    }
    int flag=0;
    for (i=0;i<N;i++){
        for (int j=i+1;j<N;j++){
            if(arr[i]==arr[j] && i!=j){
                printf("\n Duplicated number found at i=%d and j=%d number is : %d\n",i,j,arr[i]);
                flag=1;
            }
        }
        
    }
    if (flag==0){
        printf("\nNo duplicate found");
    }
}