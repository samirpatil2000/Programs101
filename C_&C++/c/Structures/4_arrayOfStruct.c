#include<stdio.h>

int main(){
    struct Student
    {
        int roll_number;
        char name[20];
        int age;
        char DOB[80];
    };
    struct Student student[20];

    int numberOfStudent,num;

    printf("Enter the number of student : ");
    scanf("%d",&numberOfStudent);

    for (int i = 0; i < numberOfStudent; i++)
    {
        printf("\n Enter the student name : ");
        scanf("%s",student[i].name);
        printf("\n Enter the student age : ");
        scanf("%d",&student[i].age);
        student[i].roll_number=i+1;
        printf("\n Enter the DOB : ");
        scanf("%s",student[i].DOB);
        printf("\n");
    }

    for (int i = 0; i < numberOfStudent; i++)
    {   printf("########## Student Details %d ###########",i+1);
        printf("\n Student name : %s",student[i].name);
        printf("\n Student age : %d",student[i].age);
        printf("\n Student roll_number : %d",student[i].roll_number);
        printf("\n DOB : %s",student[i].DOB);
        printf("\n");
    }

    printf("Enter the number of which student detail you wants to edit : ");
    scanf("%d",&num);
    num=num-1;
    printf("\n %s edit the student name : ",student[num].name);
    scanf("%s",student[num].name);
    printf("\n %d edit the student age : ",student[num].age);
    scanf("%d",&student[num].age);
    printf("\n %s edit the DOB : ",student[num].DOB);
    scanf("%s",student[num].DOB);
    printf("\n");

    for (int i = 0; i < numberOfStudent; i++)
    {   printf("########## Student Details %d ###########",i+1);
        printf("\n Student name : %s",student[i].name);
        printf("\n Student age : %d",student[i].age);
        printf("\n Student roll_number : %d",student[i].roll_number);
        printf("\n DOB : %s",student[i].DOB);
        printf("\n");
    }

    
}