#include <stdio.h>

void PrintMiddleLine(const char *ap_string, int a_space_count)
{
    // ���� ���̸� a_space_count ���� ������ ������ �����ϰ� '���� ������'��
    // '%-30s'���� '%-*s'�� �����߽��ϴ�.
    printf("��%-*s��\n", a_space_count, ap_string);
}

void TitleBar(const char *ap_string, int a_space_count)
{
    int i;
    // ù ��° ��
    printf("��");
    for (i = 0; i < a_space_count; i++) printf("��");
    printf("��\n");

    PrintMiddleLine("", a_space_count);            // �� ��° ��
    PrintMiddleLine(ap_string, a_space_count);     // �� ��° ��
    PrintMiddleLine("", a_space_count);            // �� ��° ��

    // ������ ��
    printf("��");
    for (i = 0; i < a_space_count; i++) printf("��");
    printf("��\n");
}

int main()
{
    // ���� 30�̰� ���ο� 'tipsware' ���ڿ��� ���� �簢�� ���!
    TitleBar("  tipsware", 30);
    // ���� 50�̰� ���ο� 'tipssoft.com' ���ڿ��� ���� �簢�� ���!
    TitleBar("  tipssoft.com", 50);
    return 0;
}