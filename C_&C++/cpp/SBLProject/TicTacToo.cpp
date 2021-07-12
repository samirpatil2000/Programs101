#include<iostream>

#define N 3
using namespace std;

// declaring global variable


bool isTy=false;
int X=10,O=0;
// bool isWin=false;

bool isFilled(int arr[N][N],int current_row,int current_column){
    if (arr[current_row][current_column] == 10 or arr[current_row][current_column] == 0){
        return true;
    }
    return false;
}

void printArray(int arr[N][N]){
    cout<<endl<<endl;
    for(int i=0;i<N;i++){
        for(int j=0;j<N;j++){
            cout<<"\t"<<arr[i][j];
        }
        cout<<endl<<endl;
    }
    cout<<endl;
}


void placeAtCorner(int arr[N][N]){
    for(int i=0;i<3;i+=2){
        if(arr[0][i] != X && arr[0][i] !=O){
            arr[0][i]= O;
            break;
        }
        else if(arr[2][i] != X && arr[2][i] !=O){
            arr[2][i]= O;
            break;
        }
    }
}


void machineTurn(int arr[N][N]){


    if( (arr[0][0]==X && arr[2][2]==X) || 
            (arr[0][2]==X && arr[2][0]==X) ){
                arr[1][1]=O;
                return ;
        }


    // Checking for row wise

    for (int i=0;i<N;i+=2){
        
        int c=(i>=2) ? i-2:2-i;

        if(arr[i][i]==X && arr[i][1]==X){
            
            arr[i][c]=O;
            break;

        }
        else if(arr[i][i]==X && arr[1][i]==X){

            arr[c][i]=O;
            break;

        }
    }

    for(int i=0;i<N;i++){
        // rows
        if(arr[i][0]==X && arr[i][2]){
            arr[i][1]=O;
            break;
        }
        // column
        else if(arr[0][i]==X && arr[2][i]==X){
            arr[1][i]=O;
            break;
        }
        else{
            // machine wining
            // place at corner
            placeAtCorner(arr);
            break;
        }
    }
    return ;
}




void takeChoice(int arr[N][N],int userNumber,string userName,int turn){
    int choice,row,column;
    
    cout<<"It's your turn "<<userName<<" "<<turn <<"\n";
    cout<<"Enter number every to place "<<userNumber<<" : ";
    cin>>choice;

    switch(choice){O
        case 1: 
            row=0; column=0; 
            break;
        case 2: 
            row=0; column=1; 
            break;
        case 3: 
            row=0; column=2; 
            break;
        case 4: 
            row=1; column=0; 
            break;
        case 5: 
            row=1; column=1; 
            break;
        case 6: 
            row=1; column=2; 
            break;
        case 7: 
            row=2; column=0; 
            break;
        case 8: 
            row=2; column=1; 
            break;
        case 9: 
            row=2; column=2; 
            break;
        default:
            cout<<"Invalid Move";
    }
    
    if(isFilled(arr,row,column)==false){
        arr[row][column] = userNumber;
        printArray(arr);
    }else{
        cout<<"Its already filled"<<endl;
        takeChoice(arr,userNumber,userName,turn);
    }
    
    // return choice;
}

/*
bool gameOverNoWin(int arr[N][N]){
    int counter=0;
    for(int row=0;row<N;row++){
        for(int col=0;col<N;col++){
            if (arr[row][col] == 10 or arr[row][col] == 0){
                    counter+=1;
            }
        }
    }
    if(counter==9){
        return true;
    }
    return false;
}
*/

bool gameOver(int arr[N][N]){

    // Checking for rows and column
    for(int row_col=0;row_col<N;row_col++){
        if ((arr[row_col][0]==arr[row_col][1] && arr[row_col][0]==arr[row_col][2]) ||
                (arr[0][row_col]==arr[1][row_col] && arr[0][row_col]==arr[2][row_col]) ){
            return true;
        }
    }

    // Checking for diagonal
    for(int dia=0;dia<N;dia+=2){
        if(dia ==1){
            if (arr[dia][dia]==arr[dia+1][dia+1] && arr[dia][dia]==arr[dia+2][dia+2]){
                return true;
            }
        }
        else{
            if (arr[dia][dia]==arr[dia-1][dia-1] && arr[dia][dia]==arr[dia-2][dia-2]){
                return true;
            }
        }
    }

    
    return false;
}


int main(){
    int Board[N][N]={1,2,3,4,5,6,7,8,9};
    string userName_1,userName_2;
    string userName;
    
    cout<<"Enter user name 1 for O : ";
    cin>>userName_1;
    cout<<"Enter user name 2 for X : ";
    cin>>userName_2;



    printArray(Board);
    int turn=0;
    while(turn<9){

        while(gameOver(Board) == false){
            if(turn ==0 || turn%2==0){
                userName=userName_1;
                // even user 0,2,4,
                takeChoice(Board,O,userName,turn); 
            }else{
                userName=userName_2;
                // even user 1,3,5,
                takeChoice(Board,X,userName,turn);
            }
            turn++;
        }
        cout<<userName<<"  Win the matched...!"<<endl;

        break;

    }

    // if (turn<=9){
        cout<<"\nNo Win Matched is ty \n"<<endl;
    // }


}
