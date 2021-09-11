#include <stdio.h>
#include <conio.h>
#include <windows.h>

void gotoxy(int x, int y){
    COORD Pos;
    Pos.X =x;
    Pos.Y=y;
    SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE),Pos);
}

int main(){
    int i;
    int x=9;
    int y=2;

    gotoxy(x,y);
    printf("%c%c",0xa6,0xa3);
    for(i=0; i<29; i++){
        printf("-");
    }
    printf("%c%c",0xa6 ,0xa4);


}