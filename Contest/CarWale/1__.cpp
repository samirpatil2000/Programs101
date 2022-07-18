#include<bits/stdc++.h>

int getMinimumOperation(int items_count, int* items){
    int operation_count = 0;
    len(items)
    for(int i=0;i< items_count;i++){
        if (items[i] % 2 != items[i + 1] % 2){
            continue;
        }
        int num = items[i + 1]
        if (num % 2 == 0){
            while num & 1 == 0{
                num = num / 2;
                operation_count++;
            }
        }
        else{
            while num & 1 == 1{
                num = num / 2;
                operation_count++;
            }
        }
        items[i + 1] = num;
    }
    return operation_count;
}

int main(){
    int items_count = 5;
    int items = {4, 10, 10, 6, 2};
    int result = getMinimumOperation(items_count, items);
    return 0;
}