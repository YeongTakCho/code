#include <stdio.h>

void PrintMiddleLine(const char *ap_string, int a_space_count)
{
    // 줄의 길이를 a_space_count 변수 값으로 수정이 가능하게 '형식 지정자'를
    // '%-30s'에서 '%-*s'로 수정했습니다.
    printf("│%-*s│\n", a_space_count, ap_string);
}

void TitleBar(const char *ap_string, int a_space_count)
{
    int i;
    // 첫 번째 줄
    printf("┌");
    for (i = 0; i < a_space_count; i++) printf("─");
    printf("┐\n");

    PrintMiddleLine("", a_space_count);            // 두 번째 줄
    PrintMiddleLine(ap_string, a_space_count);     // 세 번째 줄
    PrintMiddleLine("", a_space_count);            // 네 번째 줄

    // 마지막 줄
    printf("└");
    for (i = 0; i < a_space_count; i++) printf("─");
    printf("┘\n");
}

int main()
{
    // 폭이 30이고 내부에 'tipsware' 문자열이 적힌 사각형 출력!
    TitleBar("  tipsware", 30);
    // 폭이 50이고 내부에 'tipssoft.com' 문자열이 적힌 사각형 출력!
    TitleBar("  tipssoft.com", 50);
    return 0;
}