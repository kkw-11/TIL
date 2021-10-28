# C++의 동적 메모리 할당과 해제

## new&delete 연산자
* C언어에서는 동적 메모리를 할당하기 위해서는 malloc, free 함수를 사용했다.
```c++
char* str = (char*)malloc(sizeof(char)*n); //char타입의 메모리를 n개 생성하고 생성된 메모리의 첫 번째 주소를 포인터변수에 저장(=)한다.

free(str);
```
* C++ 에서는 new 연산자를 사용해 조금 더 간결한 코드로 동적 메모리를 할당할 수 있다.
* 해제는 free 대신에 delete 연산자를 사용한다.
```c++
char* str = new char[n]; 
delete []str; //동적 할당한 메모리 해제 free함수와 같음
```

```c++
int* prt1 = new int; //int형 변수 할당
double* prt2 = new dopuble; //double형 변수 할당
int* arr1 = new int[3] // 길이가 3인 int형 배열의 할당g
double* arr2 = new double[7] // 길이가 7인 double 형 배열의 할당


delete prt1; //앞서 할당한 int형 변수의 소멸
delete ptr2; //앞서 할당한 double형 변수의 소멸
delete []arr1; //앞서 할당한 int형 배열의 소멸
delete []arr2; // 앞서 할당한 double형 배열의 소멸
```
