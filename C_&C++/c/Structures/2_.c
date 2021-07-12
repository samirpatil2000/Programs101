#include<stdio.h>

int main(){
    typedef struct complex
    {
        int real;
        int imag;
    }COMPLEX;
    COMPLEX c1,c2,add_c,sub_c;

    int options;

    do
    {
        
        printf("\n 1 . Read the complex numbers");
        printf("\n 2 . Display the complex numbers");
        printf("\n 3 . Add the complex numbers");
        printf("\n 4 . Subtract the complex numbers");
        printf("\n 5 . EXIT ");
        printf("\nEnter your option : ");
        scanf("%d",&options);


        switch (options){
                
            case 1:
                printf("\nEnter the real and imaginary part of first complex number:");
                scanf("%d",&c1.real);
                scanf("%d",&c1.imag);
                printf("\nEnter the real and imaginary part of second complex number:");
                scanf("%d%d",&c2.real,&c2.imag);
                break;
            case 2:
                printf("\n first complex number %d+i%d:",c1.real,c1.imag);
                printf("\n second complex number %d+i%d: \n",c2.real,c2.imag);
                break;
            case 3:
                add_c.real=c1.real+c2.real;
                add_c.imag=c1.imag+c2.imag;
                printf("\n sum of complex numbers %d+i%d:",add_c.real,add_c.imag);
                break;

            case 4:
                sub_c.real=c1.real-c2.real;
                sub_c.imag=c1.imag-c2.imag;
                printf("\n sum of complex numbers %d+i%d:",sub_c.real,sub_c.imag);
                break;
            
            default:
                break;
         }

    } while (options != 5);
    return 0;
    
    
}