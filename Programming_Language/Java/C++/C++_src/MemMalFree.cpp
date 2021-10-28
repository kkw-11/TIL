#include <iostream>
#include <string.h>
#include <stdlib.h>

using namespace std;

// 길이 정보를 인자로 받아서, 해당길이의 문자열 저장이 가능한 배열을 생성하고, 그배열의 주소 값을 반환하는 함수
char* MakeStrAdr(int len){
    char* str = (char*)malloc(sizeof(char)*len);
    return str;
}

int main(void){
    char* str= MakeStrAdr(20);
    strcpy(str, "I am so happy~");
    cout<<str<<endl;
    cout<<"1"+str[14]<<endl;
    free(str);

    return 0;

}