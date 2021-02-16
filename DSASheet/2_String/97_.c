#include<stdio.h>
#include<string.h>



#define MAX 10
int arr_str1[MAX]={0},arr_str2[MAX]={0};

void arrMaker(char str[],int arr[]){
    int i=0,j=0;
    while(str[i]!='\0'){
        int cout=1;
        while(str[i+1]!='\0' && str[i]==str[i+1]){
            cout++;
            i++;
        }
        arr[j]=cout;
        j++;i++;
    }
}


void printArr(int arr[]){
    // int len=sizeof(arr)/sizeof(arr[0]);
    for(int i=0;i<MAX;i++){
        if(arr[i]!=0){
            printf("%d",arr[i]);
        }
    }
    printf("\n");
}

int main(){
    char str1[]="aabeeeeccd",str2[]="xxyeeeerrrs";
    arrMaker(str1,arr_str1);
    arrMaker(str2,arr_str2);
    printArr(arr_str1);
    printArr(arr_str2);
    int len=sizeof(arr_str1)/sizeof(arr_str1[0]);
    int flag=1;
    for(int i=0;i<len;i++){
        if(arr_str1[i]!=arr_str2[i]){flag=0;}
    }
    printf("the ans is %d\n",flag);
}