#include<stdio.h>


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
    ptr_student=&student;
    printf("\nEnter Name : ");
    scanf("%s",ptr_student->name);
    printf("\nEnter Age : ");
    scanf("%d",&ptr_student->age);
    display(ptr_student);
}