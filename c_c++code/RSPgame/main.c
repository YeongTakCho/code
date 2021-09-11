//https://m.cafe.daum.net/shcpro/DvFX/19?q=D_hSLIfnTlt550& 
//2.가위바위보 게임
//추가하고자 하는 사항 ->계정시스템 && 비밀번호
#include <stdio.h>
#include <stdlib.h>
#include <windows.h>

int rsc_game(int me, int op){
    int n=me-op;
    if(n==0){
        return 1;
    }
    if(n==1 || n==-2){
        return 2;
    }
    else if(n==2 || n==-1){
        return 0;
    }
}

int main(){
    FILE *f[4]={
        fopen("winlose.txt","a+"),
        fopen("rock.txt","a+"),
        fopen("scissor.txt","a+"),
        fopen("paper.txt","a+")
    };

    char *s1[4]={
        "win-lose",
        "rock",
        "scissor",
        "paper"
    };
    char buffer[100];
    int i,total_game,win;

    for(int j=0;j<4;j++){
        i=0,total_game=0,win=0;

        fgets(buffer,sizeof(buffer),f[j]);
        while(*(buffer+i)!=0){
            total_game++;
            if (*(buffer+i)=='1'){
                win++;
            }
            i++;
        }
        printf("%s rate: %f%%\n",s1[j],(float)win/(float)total_game*100.0);
    }
    printf("\n");

    int continue_game=1;
    int today_win=0;
    int today_game=0;
    do{
        today_game++;

        int money;
        printf("set you and apponet's money: ");
        scanf("%d",&money);
        int my_money=money, opponent_money=money;
        int betting_money;
        
        while(my_money >0 &&opponent_money >0){
            int my_shape, opponent_shape;
            int n;
            int win_draw_lose;
            printf("YOUR MONEY: %d OPPONENT MONEY: %d\n",my_money,opponent_money);
            printf("How much money do you wat to bet? : ");
            scanf("%d",&betting_money);
            
            printf("What shape are you going to make? ROCK(2) SCISSOR(1) PAPER(0) : ");
            scanf("%d",&my_shape);
            n= rand();
            opponent_shape= n-(n/3)*3;
            //rock 2 > scissor 1 > paper 0 > rock 2
            //2 win    1 draw     0 lose
            win_draw_lose=rsc_game(my_shape,opponent_shape);
            for(int i=3; i>=1; i--){
                printf("%d... ",i);
                Sleep(500);
            }
            printf("\n%s!!!\n",s1[3-opponent_shape]);
            Sleep(1000);
            if(win_draw_lose == 2){
                printf("YOU WON MONEY!!!\n");
                my_money= my_money+betting_money;
                opponent_money= opponent_money-betting_money;
                fputc('1',f[3-my_shape]);
            }
            else if(win_draw_lose ==1){
                printf("DRAW!!!\n");
            }
            else{
                printf("YOU LOSE MONEY\n");
                my_money=my_money-betting_money;
                opponent_money=opponent_money+betting_money;
                fputc('0',f[3-my_shape]);
            }
        }
        if(my_money <=0){
            printf("YOU LOSE GMAE!!!\n");
            fputc('0',f[0]);
        }
        else{
            printf("YOU WON GAME!!!\n");
            fputc('1',f[0]);
            today_win++;
        }
        printf("Do you want to continue playing? YES(1) NO(0) : ");
        scanf("%d",&continue_game);
    }while(continue_game == 1);
    printf("today game: %d  today win: %d\n",today_game,today_win);
    printf("today win rate: %f%%\n",(float)today_win/(float)today_game*100.0);
    printf("GOOD BYE\n");
    fclose(f[0]);
    fclose(f[1]);
    fclose(f[2]);
    fclose(f[3]);
    
}