#include<stdio.h>
#include<math.h>
#define MIN_VALUE -99999
#define MAX_VALUE 99999

int max(int a,int b){
    int val=b;
    if (a>b){
        val=a;
        return val;
    }
    return val;   
}
int min(int a,int b){
    int val=b;
    if (a<b){
        val=a;
        return val;
    }
    return val;   
}

float avg(int a,int b){
    return (a+b)/2;
}


float findMedian(int arr1[],int arr2[],int l1,int l2){

    int low=0,high=l1;
    
    


    

    while(low<=high){
        int partitionX=(low+high)/2;
        int partitionY=(l1+l2+1)/2-partitionX;

        

        int maxleftX=arr1[partitionX-1];
        if(partitionX==0){
            maxleftX=MIN_VALUE;
        }

        int minrightX=arr1[partitionX];
        if(partitionX==l1){
            minrightX=MAX_VALUE;
        }


        int maxleftY=arr2[partitionY-1];
        if(partitionY==0){
            maxleftY=MIN_VALUE;
        }
        int minrightY=arr2[partitionY];
        if(partitionY==l2){
            minrightY=MAX_VALUE;
        }

        if(maxleftX<=minrightY && maxleftY<=minrightX){
            if((l1+l2)%2 ==0){
                float value=avg(max(maxleftX,maxleftY),min(minrightX,minrightY));
                return value;
            }else{
                printf("the maxleftX = %d maxleftY = %d\n",maxleftX,maxleftY);
                return max(maxleftX,maxleftY);
            }
        }
        else if(maxleftX>minrightY){
            high=partitionX-1;
            printf("%d\n",high);
        }else{
            low=partitionX+1;
            printf("%d\n",low);
        }
    }


    
}

int main(){
    int arr1[] = {1, 2, 3, 4, 5, 6, 7, 8, 9},arr2[] = { 10,11, 12, 13, 14, 15, 16, 17, 18, 19 };
    int l1=sizeof(arr1)/sizeof(arr1[0]),l2=sizeof(arr2)/sizeof(arr2[0]);
    printf("%d %d \n",l1,l2);

    printf(" the median is %2.f\n",findMedian(arr1,arr2,l1,l2));
    // printf("The avg of 3 4 is %d \n",min(6,8));

}