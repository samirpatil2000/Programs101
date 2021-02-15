#include<stdio.h>


int main(){
    char char_arr[]="IVXLCDM";
    char input[]="CV";
    int num_arr[]={1,5,10,50,100,500,1000};

    int i=0,output=0;
    while(input[i] != '\0'){
        for(int j=0;j<7;j++){
            if(input[i]==char_arr[j]){
                int k=j;
                while(k>=1 && input[k-1]==char_arr[0]){
                    output-=2;
                    k--;
                }
                output+=num_arr[j];
            }
        }
        i++;
    }
    printf("The output is : %d\n",output);
} 