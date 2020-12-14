#include<stdio.h>

struct Student
{
    int age;
    char name[20];
};





int main(){
    struct Student student,*ptr_student;
    ptr_student=&student;

    printf("\n Enter the details of the student : ");
    printf("\n Age : ");
    scanf("%d",&ptr_student->age);
    printf("\n Enter the name : ");
    scanf("%s",ptr_student->name);

    printf("\n Name : %s",ptr_student->name);
    printf("\n Age : %d\n",ptr_student->age);
}