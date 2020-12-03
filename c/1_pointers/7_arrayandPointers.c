#include<stdio.h>

int main(){
    
    int arr[10]={1,2,3,4,5};

    int *ptr,i;
    ptr=&arr[2];  // this pointer ptr is pointing towards 3rd element of array arr
    *ptr=-1;      // replacing 3rd element  3  to  -1


    ptr+=1;     // increamenting pointing element by 1
    *ptr=-1;    // replacing 4th element 4 to -1

    *(ptr+1)=0;   // replacing 5ht element 5 to 0

    for(i=0;i<5;i++){
        printf("\t %d",*(arr+i));
    }
    printf("\n");
    printf("%d\n",*(arr+1));
    printf("%d\n",*(ptr+1));
    


}