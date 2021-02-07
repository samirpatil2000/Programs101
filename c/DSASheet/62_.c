#include<stdio.h>
#include<string.h>
#define MAX 100
// PYTHON

char countAndSay(int n){
    if(n==1){
        return "1"; 
    }else{
        int i=0;
        char a[MAX]=countAndSay(n-1);
        char new[MAX];

        while(a[i]!='\0'){
            int count=1;
            char a=(str)a[i];
            while(a[i+1]!='\0'&& a[i]==a[i+1]){
                count++;i++;
            }
            char b=(str)count;
            char c=strcat(b,a);
            new=strcat(new,c);
            i++;
        }
        return new;
    }
}

int main(){
    int num;
    printf("\nEnter the number :");
    scanf("%d",&num);
    printf("the answer is : %c ",countAndSay(num));
}