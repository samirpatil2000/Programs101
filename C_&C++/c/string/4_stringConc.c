#include<stdio.h>

int main(){
    
    char first[100],second[100];


    printf("\nEnter first text : ");
    // scanf("%s",first);
    gets(first);   // gets method take space as well 
    


    printf("\nEnter second text : ");
    // scanf("%s",second);
    gets(second);

    // first find the length of first string 
    int i=0,j=0;
    int length_of_first;
    while(first[i] != '\0'){
        i++;
    }
    length_of_first=i;
    while (second[j] != '\0'){
        first[length_of_first]=second[j];
        length_of_first++;
        j++;
    }
    first[length_of_first]='\0';


    printf("\n And the concatination is : ");
    puts(first);
    

}