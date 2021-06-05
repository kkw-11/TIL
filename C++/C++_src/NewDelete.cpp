#include <iostream>
#include <string.h>

using namespace std;

char* MakeStrAdr(int len){

    // char* str = (char*)malloc(sizeof(char)*len));
    char* str = new char[len]; // char 타입의 변수 len만큼 생성하여 첫번째 주소를 str에 저장, malloc함수의 void 포인터 반환을 형변환해주어야 하는 불편함 없앰

    return str;
}

int main(void){
    char* str = MakeStrAdr(20);

    strcpy(str,"I am so happy~~");
    cout<<str<<endl;
    // free(str);
    delete []str;

    return 0;
}