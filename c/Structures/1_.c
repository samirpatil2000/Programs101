#include<stdio.h>

// read and display structures

int main(){
    struct student
    {
        int roll_number;
        int avg_marks;
        char name[20];
        char class[20];
    };
    struct student std_1;

    printf("Enter the following details :\n");
    printf("\nname : ");
    gets(std_1.name);
    printf("\nclass_name : ");
    gets(std_1.class);
    printf("\navg_marks : ");
    scanf("%d",&std_1.avg_marks);
    printf("\nroll_number : ");
    scanf("%d",&std_1.roll_number);

    printf("\nPrinting Student Details :");


    printf("\nname : %s",std_1.name);
    printf("\nclass_name : %s",std_1.class);
    printf("\navg_marks : %d",std_1.avg_marks);
    printf("\nroll_number : %d\n",std_1.roll_number);    


    
}