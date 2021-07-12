#include<stdio.h>
#include<stdlib.h>


struct Student 
{
    int age;
    char name[20];
};

void display(struct Student *ptrStudent){
    printf("\nName : %s",ptrStudent->name);
    printf("\nAge : %d\n",ptrStudent->age);
}



int main(){
    struct Student *ptr_student,student;


    // ptr_student=&student; // or u can do 
    ptr_student=(struct Student *)malloc(sizeof(struct Student));


    printf("\nEnter Name : ");
    scanf("%s",ptr_student->name);
    printf("\nEnter Age : ");
    scanf("%d",&ptr_student->age);
    display(ptr_student);
}