#include<stdio.h>
#define N 3000
#include<math.h>

int main(){
    int arr[N]={0};
    arr[0]=arr[1]=1;

    // int sqrts=(int)sqrt(N);


    for(int i=2;i*i<=N;i++){
        for(int j=i*2;j<N;j+=i){
            arr[j]=1;
            // printf("%d\n",j);
        }
    }

    printf("Printing array\n");
    
    for(int i=2;i<N;i++){
        if(arr[i]==0){
            printf(" %d\t",i);
        }
        
    }
    printf("\n");


}