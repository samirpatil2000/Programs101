#include<stdio.h>

int main(){
    int a[]={5 ,6 ,7};
    int b[]={3 ,6 ,10};
    int result_count[2]={0};
    int a_counter=0,b_counter=0;
    int return_arr[2]={0};
    for(int i=0;i<3;i++){
        if (a[i]>b[i]){
            a_counter+=1;
        }else if (a[i]<b[i]) {
            b_counter+=1;
        }
    }
    result_count[0]=a_counter;
    result_count[1]=b_counter;


    for(int i=0;i<2;i++){
        printf("\t%d",result_count[i]);
    }
    printf("\n");

}