#include<stdio.h>

// int insertionSort(int arr[],int len){

//     for(int i=1;i<len;i++){
//         int temp=arr[i];
//         int j=i-1;
//         while ( j>=0 && arr[j]>temp){
//             arr[j+1]=arr[j];
//             j--;
//         }
//         arr[j+1]=temp;
//     }
// }

void printArray(int arr[],int len){
    for(int i=0;i<len;i++){
        printf("\t %d",arr[i]);
    }
    printf("\n");
}


void optimium(int arr[],int len){
    // solution by samir patil
    int i=0;
    int arr_len=len;
    printf("Sticks = %d\n",arr_len);
    while(i<len){
        int rep=1;
        while(i+1<len && arr[i]==arr[i+1]){
            rep++;
            i++;
        }
        i++;
        if(rep != arr_len){
            printf("Sticks = %d\n",arr_len=arr_len-rep);
        }
        
    }
}


void brute(int arr[],int len){
    for(int i=0;i<len;i++){
        int count=0;
        int min_stick_length=arr[i];
        if(arr[i]>0){
            for(int j=i;j<len;j++){
                if(arr[j]>0){
                    count++;
                    arr[j]=arr[j]-min_stick_length;
                }
            }
            printArray(arr,len);
        }
        if(count!=0){
            printf("%d ",count);
        }
    }
}

int main(){
    int arr[]={2,2,2,2};
    // int arr[]={2,5,5,5,6,7,8};
    // consider array is sorted 
    int len=sizeof(arr)/sizeof(arr[0]);
    printArray(arr,len);
    // brute(arr,len);
    // printArray(arr,len);
    printf("Optimium Solution\n");
    optimium(arr,len);
    
}