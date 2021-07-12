#include<stdio.h>



int main(){
    char names[5][10],temp[10];
    int n;

    printf("Enter number of student : ");
    scanf("%d",&n);

    for(int i=0;i<n;i++){
        printf("\nEnter  student name :   ",i+1);
        gets(names[i]);
    }

    for(int i=0;i<n;i++){
        // printf("\n");
        puts(names[i]);
    }
    

}