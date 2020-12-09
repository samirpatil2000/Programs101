#include<stdio.h>
#include<string.h>


int main(){
    char str_1[100],str_2[100];
    printf("\nEnter str_1 : ");
    gets(str_1);
    printf("\nEnter str_2 : ");
    gets(str_2);

    int len_1=strlen(str_1),len_2=strlen(str_2),i=0,same=0;
    

    if(len_1==len_2){
        while (i<len_1){
            if(str_1[i]==str_2[i]){
                i++;
            }
            else{
                break;
            }
        }
        if (i==len_1){
            same=1;
            printf("Both strigs are equal\n");
        }
    }
    }

}