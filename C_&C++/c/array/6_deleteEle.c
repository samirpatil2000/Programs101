#include<stdio.h>

int main(){
    
    int n=10;
    int arr[10]={78,54,59,87,84,98,34,58,53,99};

    printf("\nPrinting the array before deleting");
    printf("\n");
    for(int i=0;i<n;i++){
        printf("arr[%d]= %d\n",i,arr[i]);
    }

    int elementToBeDelete=59;
    for(int i=0;i<n;i++){
        if (elementToBeDelete==arr[i]){
            for (int j=i;j<n;j++){
                arr[j]=arr[j+1];
            }
        }
    }
    n-=1;
    printf("\nPrinting the array After Deleting");
    printf("\n");
    for(int i=0;i<n;i++){
        printf("arr[%d]= %d\n",i,arr[i]);
    }
}