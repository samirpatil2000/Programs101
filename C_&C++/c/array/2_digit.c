#include<stdio.h>
#include<math.h>

// To enter n number of digits.Form a number usng these digits
# define N 4

int main(){
    int digit[10],n,i;
    printf("Enter the number of digits : ");
    scanf("%d",&n);
    
    for(i=0;i<n;i++){
        printf("\n Enter the element at %d : ",i+1);
        scanf("%d",&digit[i]);
    }
    printf("Printing the number from these  array digits :\n");

    int number=0;
    for (i=0;i<n;i++){
        // printf("%d\n",digit[i]);
        number=number+digit[i]*pow(10,i);
    }
    printf("\nNumber = %d\n",number);
}