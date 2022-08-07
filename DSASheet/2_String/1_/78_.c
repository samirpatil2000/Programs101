#include<stdio.h>
#include<string.h>

#define row 6 
#define col 6



int search(char arr[row][col],char str[],int i,int j,int count){
    int found=0;
    char temp;
    
    if( i<row || j<col || i>0 || j>0 || arr[i][j] == str[count]){
        count++;
        temp=arr[i][j];
        arr[i][j]='0';
        if(count==strlen(str)){
            found=1;
        }else{
            
            count++;
            found+=search(arr,str,i,j-1,count);
            found+=search(arr,str,i,j+1,count);
            found+=search(arr,str,i+1,j,count);
            found+=search(arr,str,i-1,j,count);
            
        }
        arr[i][j]=temp;
    }
    
    return found;
}

int main(){
    char arr[row][col]={ 
                   "BBABBM",  
                   "CBMBBA",  
                   "IBABBG",  
                   "GOZBBI",  
                   "ABCBBC",  
                   "MCIGAM" };

    char str[]="MAGIC";
    // printf("the test arr[%d][%d] == %c \n",1,0,arr[1][0]);

    int counter=0;
    for(int i=0;i<row;i++){
        for(int j=0;j<col;j++){
            printf("arr[%d][%d] == %c \n",i,j,arr[i][j]);
            if(arr[i][j]==str[0]){
                counter+=search(arr,str,i,j,0);
            }
            
        }
    }
    printf("The Counter is %d\n",counter);
}