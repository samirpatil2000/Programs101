#include<stdio.h>


int main(){
    int arr[]={1, 3, 4, 5, 7};
    int len=sizeof(arr)/sizeof(arr[0]);
    int X=12,count=0;
    
    for(int i=0;i<len-2;i++){
        int low=i+1,high=len-1;
        while (low<high){
            if(arr[i]+arr[low]+arr[high]<X){
                printf("%d %d %d\n",arr[i],arr[low],arr[high]);
                count+=(high-low);
                low++;
            }else{
                high--;
            }
        }
        // if(low>high){
        //     break;
        // }
    }
    printf("The count %d\n",count);
}