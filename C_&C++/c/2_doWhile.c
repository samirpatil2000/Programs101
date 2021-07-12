#include<stdio.h>

int main(){

    int options;

    do
        {
            
            printf("\n 1 . Read the complex numbers");
            printf("\n 2 . Display the complex numbers");
            printf("\n 3 . Add the complex numbers");
            printf("\n 4 . Subtract the complex numbers");
            printf("\n 5 . EXIT ");
            printf("Enter your option : ");
            scanf("%d",options);

        } while (options != 5);

}
