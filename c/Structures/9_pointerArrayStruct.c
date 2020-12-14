#include<stdio.h>

struct Student
{
    int age;
    char name[20];
};



int main(){
    int i,n;

    struct Student *ptr[10];

    printf("Enter the number of student : ");
    scanf("%d",&n);


    for(int i=0;i<n;i++){

        printf("\nEnter the name : ");
        scanf("%s",ptr[i]->name);
        // gets(ptr[i]->name);
        printf("\nEnter the age : ");
        scanf("%d",&ptr[i]->age);

    }


    for(int i=0;i<n;i++){

        printf("\nEnter the name : %s",ptr[i]->name);
        printf("\nEnter the age : %d\n",ptr[i]->age);

    }

    
}