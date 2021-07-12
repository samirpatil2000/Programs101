#include<stdio.h>


void unsortedArray(int arr[],int len,int target){
// Solution By Samir Patil
    for(int i=0;i<len;i++){
        for(int j=0;j<len;j++){
            int sum=arr[i]+arr[j];
            if(target==sum){
                printf("The pair ares %d , %d \n",arr[i],arr[j]);
                return;
            }
        }
    }
}

void sortedArray(int arr[],int len,int target){
// Solution By Samir Patil
    int low=0,high=len-1,sum;
    while(low<high){
        sum=arr[low]+arr[high];
        if(sum==target){
            printf("The pair ares %d , %d \n",arr[low],arr[high]);
            break;
        }else if(target>sum){
            low++;
        }else{
            high--;
        }
    }
}


int main(){
    int arr[]={-1,2,5,6,7,10};
    int target=11;

    int len=sizeof(arr)/sizeof(arr[0]);
    sortedArray(arr,len,target);
    unsortedArray(arr,len,target);

}