#include<stdio.h>
#include<string.h>

int method_1(char str1[],char str2[]){
    int pos,i=0,j=0,len=strlen(str1),flag=1;


    if(strlen(str1) != strlen(str2)){
        flag=0;
        return flag;
    }
    while(str1[i] != '\0'){
        if(str1[0]==str2[i]){
            pos=i;
            break;
        }
        i++;
    }
    printf("%d\n",pos);
    while(str1[j] != '\0'){
        // printf("%c and %c\n",str1[j],str2[pos]);
        if(str1[j]==str2[pos]){
            j++;
            pos++;
            if(pos>len-1){
                pos=0;
            }
        }else{
            flag=0;
            return flag;
        }
    }
    return flag;
}



int method_2(char str1[],char str2[]){
    /*
    1. Create a temp string and store concatenation of str1 to
       str1 in temp.
                          temp = str1.str1
    2. If str2 is a substring of temp then str1 and str2 are 
       rotations of each other.

    Example:                 
                     str1 = "ABACD"
                     str2 = "CDABA"

     temp = str1.str1 = "ABACDABACD"
     Since str2 is a substring of temp, str1 and str2 are 
     rotations of each other.
    */
}

int main(){
    char str1[100],str2[100];
    printf("Enter the strings \n");
    scanf("%s\n%s",str1,str2);


    printf("The ans is : %d\n",method_1(str1,str2));



}