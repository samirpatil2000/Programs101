#include<stdio.h>

int getMinDiff(int arr[], int n, int k) {
        int max=arr[0],min=arr[0];
        for (int i=0;i<n;i++){
            if(arr[i]>max){
                max=arr[i];
            }
            if(arr[i]<min){
                min=arr[i];
            }
        }
        return max-min-2*k;
}


int main(){
    
    int arr[]={3, 9, 12, 16, 20};

    int num=getMinDiff(arr,5,3);
    printf("%d\n",num);

}