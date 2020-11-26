#include<stdio.h>


int search(int l,int r,int list[],int n){
    int flag=0;
    int mid=l+r/2;

    if(n==list[mid]){
        return flag=1;
    }

    while (l<r)
    {
        if(n<list[mid]){
            
            return search(l,mid-1,list,n);
        }
        else{
        
            return search(mid+1,r,list,n);
        }
    }
    
}

int main(){
    int n=10;
    int number=1;
    int arr[n];
    for(int i=0;i<n;i++){
        // printf("\narr[%d]=",i);
        // scanf("%d",&arr[i]);
        arr[i]=i;
    }
    for(int i=0;i<n;i++){
        printf("\narr[%d]=%d",i,arr[i]);

    }
    int l=0,r=n-1;
    int flag=search(l,r,arr,number);
    printf("\n%d\n",flag);

}