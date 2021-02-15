#include<stdio.h>




int main(){
    char visited[26]={0};
    char str[]="ABCBCADEED";
    int n=1,occupied=0,nogetcomp=0;
    int i=0;
    while (str[i] != '\0'){
        int index=(str[i]-'A');
        printf("The index is %d\n",index);
        if(visited[index]==0 && occupied<n ){
            visited[index]=1;
            occupied++;
        }else if(visited[index]==1 && occupied<=n){
            visited[index]=0;
            occupied--;
        }else{
            nogetcomp++;
        }
        i++;
    }
    printf("The ans %d\n",nogetcomp/2);
    
}