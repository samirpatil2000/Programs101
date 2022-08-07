#include<stdio.h>



void hashing(char str[],int len){
    int hash[123]={0};
    int length=len;
    char result[len];

    for (int i = 0; i < len; i++)
    {
        if (hash[str[i]] == 0)
        {
            hash[str[i]]=1;
            // result=+str[i];
        }
    }
    
}

int main(){

    char str[100],new_str[100];
    
    printf("\nEnter the string : ");
    gets(str);
    
    int len=strlen(str);
    printf("%d\n",len);

    for(int i=0;i<len;i++){
        int count=0;
        for (int j = i+1; j<len; j++)
        {
            if(str[i]==str[j] && str[i] !='$' && str[j] !='$'){
                count++;
                str[j]='$';
            }
        }
        if( str[i] != "$" && count>0){
            printf("%c - %d\n",str[i],count+1);
        }
    }
}