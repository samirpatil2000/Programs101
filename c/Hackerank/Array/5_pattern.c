/*   #
    ##
   ###
  ####
 #####
######
*/

#include<stdio.h>

int main(){
    int n=6;
    printf("*");
    for(int i=0;i<n;i++){
        printf("\n");
        for(int j=n-i-1;j>0;j--){
            printf(" ");
            // printf("\t #");
        }
        for(int k=0;k<=i;k++){
            printf("#");
        }
        printf("\n");
    }
    printf("#");
    printf("\n");
    

}