#include<stdio.h>

typedef struct 
    {
        int x;
        int y;
    }Point;

void passingIndividualMembers(int a,int b){
    printf("%d  %d\n",a+1 ,b-2);
}

void PassingEntireFunction(Point P){
    printf("The cordinate of the points are : %d %d\n",P.x,P.y+9);
}
int main(){
    Point ptn={2,3};
    passingIndividualMembers(ptn.x,ptn.y);

    printf("\nPassingEntireFunction \n");
    PassingEntireFunction(ptn);

    
}