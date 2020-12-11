#include<stdio.h>
#include<string.h>

char text[200],replaced_str[50],add_str[50],new_str[200];




int bySimpleMethod(int M,int N_RE,int N_AD){
    int copy_loop=0,a=0,n;
    for (int i=0;i<=M-N_RE;i++){

        int j=0;
        for (j=0;j<N_RE;j++){
            if(text[i+j] != replaced_str[j]){
                break;
            }
        }
        if(replaced_str[j]=='\0'){
            copy_loop=i+j;
            while(add_str[a] != '\0'){
                new_str[n]=add_str[a];
                n++;
                a++;
            }
        }
        new_str[n]=text[copy_loop];
        copy_loop++;
    }
}


int main(){
    

    printf("\nEnter text : \n");
    gets(text);
    printf("\nEnter string to replaced  : \n");
    gets(replaced_str);
    printf("\nEnter string to add  : \n");
    gets(add_str);

    
    int len_str=strlen(text),len_replaced_str=strlen(new_str);


    int i=0,n=0,copyloop=0;
    while(text[i] != '\0'){
        int k=i,j=0;
        while(text[k]==replaced_str[j] && replaced_str[j] !='\0'){
            k++;
            j++;
        }
        if(replaced_str[j]=='\0'){
            int a=0;
            copyloop=k;

            while(add_str[a] !='\0'){
                new_str[n]=add_str[a];
                n++;
                a++;
            }
        }
        new_str[n]=text[copyloop];
        copyloop++;
        n++;
        i++;
    }
    puts(new_str);
}