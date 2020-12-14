#include<stdio.h>

int main(){
    typedef struct
    {
        int year;
        int month;
        int day;
    }DOB;
    typedef struct
    {
        char first_name[20];
        char last_name[20];
    }Name;

    struct Student
    {
        Name name;
        DOB birthdate;  
        int roll_number;
    };
    struct Student student;

    printf("\n Enter the age : ");
    scanf("%d",&student.roll_number);
    printf("\n Enter the first name : ");
    scanf("%s",student.name.first_name);
    printf("\n Enter the last name : ");
    scanf("%s",student.name.last_name);

    printf("\n Enter the date of birth (DD MM YY) : ");
    scanf("%d%d%d",&student.birthdate.day,&student.birthdate.month,&student.birthdate.year);

    printf("\t \t \t Printing details  \n");
    printf("Name : %s %s",student.name.first_name,student.name.last_name);
    printf("\nAge : %d",student.roll_number);
    printf("\nBirthdate : %d/%d/%d\n",student.birthdate.day,student.birthdate.month,student.birthdate.year-1900);
    
    
    
    
}