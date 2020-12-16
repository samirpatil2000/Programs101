#include<stdio.h>
#include<stdlib.h>

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

        ptr[i]=(struct Student *)malloc(sizeof(struct Student));


        printf("\nEnter the name : ");
        scanf("%s",ptr[i]->name);
        // gets(ptr[i]->name);
        printf("\nEnter the age : ");
        scanf("%d",&ptr[i]->age);

    }


    for(int i=0;i<n;i++){

        printf("The Name and Age : %s   %d\n",ptr[i]->name,ptr[i]->age);

    }

    
}