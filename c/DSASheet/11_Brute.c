#include<stdio.h>



void printArray(int arr[],int n){
    printf("\n");
    for (int i = 0; i < n; i++)
    {
        printf("\t %d",arr[i]);
    }
    printf("\n");
}


int main(){
    int arr1[] = { 1,2,3,4,5,6,7,8};

    int arr2[] = {12,9,84,43,54,34};

    int new_array[]={};

    int n = sizeof(arr1) / sizeof(arr1[0]);
    int m = sizeof(arr2) / sizeof(arr2[0]);
    printArray(arr1,n);
    printArray(arr2,m);

    int length=0;
    for (int co=0;co<n;co++){
        new_array[co]=arr1[co];
        length++;
    }
    int k=length;
    for(int i=0;i<m;i++){
         
        int j=0;
        while (j<n)
        {
            if(arr2[i] == new_array[j]){
                break;
            }
            j++;
        }
        printf("%d\n",j);
        if (j==n)
        {
            new_array[k]=arr2[i];
            k++;
            // printf("%d %d \n",k,i);
        }
        
    }
    printArray(new_array,k);

}

//https://www.freelancer.in/projects/php/build-social-media-website-28680696/details