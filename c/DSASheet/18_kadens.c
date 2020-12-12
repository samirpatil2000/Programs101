#include<stdio.h>



int kadensAlgo(int arr[10]){
    int max=arr[0],current_sum=0;;
    for(int i=0;i<10;i++){
        current_sum+=arr[i];
        if(max<current_sum){
            max=current_sum;
        }
        if(current_sum<0){
            current_sum=0;
        }
    }
    return max;
}
int usingBrute(int arr[10]){
    int max=arr[0];
    
    for(int i=0;i<10;i++){
        for(int j=i;j<10;j++){
            
            int current_sum=0;
            for(int k=i;k<=j;k++){
                current_sum+=arr[k];
            }
            if(current_sum>max){
                max=current_sum;
            }
        }
    }
    return max;


}

int main(){
    int arr[10]={2,-3,4,5,-2,1,0,6,-7,8};
    printf("using brute force %d\n",usingBrute(arr));
    printf("using kadens algo %d\n",kadensAlgo(arr));
}