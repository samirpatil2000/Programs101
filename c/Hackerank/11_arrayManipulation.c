#include<stdio.h>
int printArray(int arr[10]){
    printf("\n");
    for (int i=0;i<10;i++){
        printf("\t %d",arr[i]);
    }
    printf("\n");
}


int main(){
    int n=10;
    int queries[3][3]={
                //   a b k
                    {1,5,3},
                    {4,8,7},
                    {6,9,1}
                };
    int arr[10]={0};

    int size=10,i;
    // int arr[size];
    // for(i=0;i<size;i++)
    // {
    //     arr[i]=0;
    // }







    printf("\nPrinting initial array");
    printArray(arr);
    for (int i=0;i<n;i++){
        int a,b,k;
        a=queries[i][0];
        b=queries[i][1];
        k=queries[i][2];
        int start_q_index=a-1,end_q_index=b-1;
        while(start_q_index<=end_q_index){
            arr[start_q_index]+=k;
            start_q_index++;
        }
        printArray(arr);

    }
    printf("\nPrinting final array\n");
    printArray(arr);

    int max=arr[0];
    for(int i=1;i<size;i++){
        if(arr[i]>max){
            max=arr[i];
        }
    }
    printf("\n the max is %d\n",max);

}