#include<stdio.h>
#include<math.h>


/*1.
int arr[]={3254,2874,9745,120534};
    int t;
    scanf("%d",&t);
    while(t-->0){
        int n;
        scanf("%d",&n);
        printf("%d",arr[n-1]);
    }
    
*/

int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    int t;
    scanf("%d",&t);
    while(t-->0){
        int n;
        scanf("%d",&n);
        int arr[2*n];
        int max=n;
        for(int i=0;i<2*max;i++){
            scanf("%d",&arr[i]);  
        }
        int count=0;
        for(int i=0;i<max;i++){
            for (int j=max;j<2*max;j++){
                if(arr[i]==arr[j]){
                    count++;
                }
            }
        }
        // printf("%d\n",count);
        if(count==max){
            printf("PRESENT\n");
        }else{
            printf("NOT PRESENT\n");
        }
    }
    return 0;
}