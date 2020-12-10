#include<stdio.h>




int search(int l,int r,int list[10],int n){
    int flag=0;
    int mid=l+r/2;

    while (l<=r){

        if(n==list[mid]){
            return 1;
        }
        if(n<list[mid]){
            
            return search(l,mid-1,list,n);
        }
        else{
        
            return search(mid+1,r,list,n);
        }
    }
    return 0;

    
}

int main(){
    int n=10;
    int number=8;
    int arr[n];
    for(int i=0;i<n;i++){
        // printf("\narr[%d]=",i);
        // scanf("%d",&arr[i]);
        arr[i]=i;
    }
    for(int i=0;i<n;i++){
        printf("\narr[%d]=%d",i,arr[i]);

    }
    printf("\n");
    int l=0,r=n-1;
    int flag=search(l,r,arr,number);
    printf("\n%d\n",flag);

}