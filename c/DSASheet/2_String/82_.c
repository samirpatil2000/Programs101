#include<stdio.h>
#include<string.h>
#define row 3 
#define col 6


int main(){
    char arr[row][col]={"flower","flow","flight"};
    char out[]="";
    char temp;
    
    for (int j = 0; j < col; j++){
        int i = 0,n=j;
        temp=arr[0][j];
        // printf("%c\n",temp);
        // strcpy(arr, val);
        while (arr[i][j] == temp && i<=row)
        {
            i++;
            // printf("%d\n",i);
        }
        if(i == row){
            printf("%c\t",arr[0][j]);
            // strcat(out,temp);
            // out=out+temp;
        }else{
            break;
        }

    }
    printf("The common prefix is %s\n",out);
    
}