#include<stdio.h>
# define N 10

int main(){
    int arr[N],n,i=0;
    
    // for(i;i<N;i++){
    //     arr[i]=i*2+4;
    // }
    for(i=0;i<N;i++){
        scanf("%d",&n);
        arr[i]=n;
    }
    printf("The array is :\n");
    for (i=0;i<N;i++){
        printf("%d\n",arr[i]);
    }
    printf("The reversing the array:\n");
    for (i=0;i<N;i++){
        printf("%d\n",arr[N-i]);
    }

    int counter=0;

    for (int j=0;j<N;j++){
        for (i=1;i<N;i++){
            if (arr[j]==arr[i]){
                printf(" %d numbers\n",counter+1);
            }
            // else{
            //     printf("Nothing is common ");
            // }
            
        }
    }


}