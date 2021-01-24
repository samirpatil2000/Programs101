#include<stdio.h>
#include<stdlib.h>


struct student{
    int data;
    char name[20];
};
struct student *ptr_student[10];


int main(){
    int i,n;
    printf("\nEnter the number of student : ");
    scanf("%d",&n);
    for(int i=0;i<n;i++){
        ptr_student[i]=malloc(sizeof(struct student));
        printf("\nEnter the name %d ",i+1);
        scanf("%s",ptr_student[i]->name);
        printf("\nEnter the number ");
        scanf("%d",&ptr_student[i]->data);
    }
    printf("\nPRINTING DETAILS..");
    for(int i=0;i<n;i++){
        printf("\n Name = %s",ptr_student[i]->name);
        printf("\n Number = %d",ptr_student[i]->data);
    }
}