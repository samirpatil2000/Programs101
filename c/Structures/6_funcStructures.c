#include<stdio.h>

typedef struct distance
{
     int kms;
     int meters;
}Distance;



Distance addDistance(Distance d1,Distance d2){
    Distance sum;
    sum.meters=d1.meters+d2.meters;
    sum.kms=d1.kms+d2.kms;
    if (sum.meters>=1000)
    {
        sum.meters=sum.meters%1000;
        sum.kms+=1;
    }
    
    return sum;
}

Distance subDistance(Distance d1,Distance d2){
    Distance sub;
    if(d1.kms>d2.kms){
        sub.kms=d1.kms-d2.kms;
        sub.meters=d1.meters-d2.meters;
    }else{
        sub.kms=d2.kms-d1.kms;
        sub.meters=d2.meters-d1.meters;
    }
    if(sub.meters<0){
        sub.kms=sub.kms-1;
        sub.meters=sub.meters+1000;
    }
    return sub;
}

int main(){
    int option;

    Distance D1,D2,addition,sub;

    do
    {
        printf("\n 1 . Read the distance's");
        printf("\n 2 . Display the distance's");
        printf("\n 3 . Add the distance's");
        printf("\n 4 . Subtract the distance's");
        printf("\n 5 . EXIT ");
        printf("\nEnter the option : ");
        scanf("%d",&option);

            
        switch (option){
            case 1:
                printf("Enter the first distance : \n");
                scanf("%d %d",&D1.kms,&D1.meters);
                printf("Enter the second distance : \n");
                scanf("%d %d",&D2.kms,&D2.meters);
                break;
            case 2:
                
                printf("First distance : %dkm %dmeter\n",D1.kms,D1.meters);
                printf("Second distance : %dkm %dmeter\n",D2.kms,D2.meters);
                break;

            case 3:
                addition=addDistance(D1,D2);
                printf("Addition of two distances is : %dkm %dmeter \n",addition.kms,addition.meters);
                break;

            case 4:
                sub=subDistance(D1,D2);
                printf("Substration of two distances is : %dkm %dmeter \n",sub.kms,sub.meters);
                break;
        
            default:
                break;
        } 

    } while (option != 5);



    

}