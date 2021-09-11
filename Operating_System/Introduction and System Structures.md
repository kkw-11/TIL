# Operating System 
* 운영체제는 자원(하드웨어자원, 소프트웨어자원(컴퓨터 구조 내부 버스를 타고 돌아다니는 모든 신호 포함))을 관리해주고 응용프로그램에, 사용자에 인터페이스를 제공해주는 소프트웨어
* 다른 프로그램(응용프로그램)은 하나의 main함수를 가지고 있지만 운영체제 소프트웨어는 main함수를 가지고 있지 않다.
* 시스템 소프트웨어 과목에서 프로그램마다 스택을 가지는데 어떻게 관리 되는지 이해하고 잇어야하고 캐시메모리, 링킹 등의 선수 지식도 필요하다.
* 운영체제는 하드웨어와 소프트웨어 자원을 관리하는 시스템 소프트웨어, 소프트웨어라는 것을 잊지 말자!
* 최초의 운영체제는 하드웨어 IO디바이스의 처리를 하기위해 등장했음, 그전에는 모든 I/O device도 모두 사람이 직접 코드를 입력해서 작성했지만 이러한 작업은 대신해주는 소프트웨어가 있길 바랐기 때문에 운영체제가 그역할을 하면서 운영체제가 등장 했음
* 보안, 네트워킹도 운영체제의 역할
* 네트워크의 TCP/IP계층이 운영체제 레이어 이다. MAC은 LAN 카드 하드웨어 레이어
* H/W detail을 처리함 host로서, app(guest)이 하는 요청을 처리해줌(디스크 공간상에 file이 어디 있는지는 app이 몰라도 됨 host인 OS가 처리해줌)

## 학습 목적
* 개발자로서 프로그램을 만들면서 시스템이 어떻게 동작하는지 이해하고 더 효율적인 소프트웨어를 만들수 있도록 하는 것
* 모든 프로그램은 자기의 스택을 갖는데 이러한 스택이 어떻게 manage 되는지 시스템소프트웨어 과목에서 배움

## Process Subsystem
* concept and management
* Scheduling
* Synchronization
* Deadlock
## File Subsystem
* File System Organization
* File System Implementation
## Memory Subsystem
* Main Memory Management
* Virtual Memory Management

## IO management


## 주요 용어정리
* System Call은 Application이 운영체제안에 있는 함수를 사용하여 어떠한 작업을 하도록 요청하는것 디스크에 있는 어떤 자료를 읽어와라 등의 task
    * c 프로그래밍에서 main함수가 다른 함수를 사용하는 function call작업과 같음 다만 App이 운영체제의 함수를 사용하는 것을 특별히 system call이라고 함
* Interrupt는 H/W가 운영체제에 요청하는것을 Interrupt라고 함

## Single User system과 Multi User system의 차이점
* Multi User system은 Proection mechanism이 필수 다른 사용자의 파일에 접근하는 것을 막아야함

## Single Tasking 과 Multi Tasking system의 차이점
* Concurrency Control, Synchronization mechanisms은 Multi Tasking의 필수 조건임
    * Concurrency - 운영체제의 스케줄링 알고리즘에 따라 여러작업을 빠르게 전환하면서(Context Switch)하면서 한개의 코어에서도 어려작업을 실제로 동시에 실행하는 것처럼 보이는것 (물리적으로 동시가 아님)

## 리눅스의 새로운 프로세스를 생성하는 함수
* fork(), clone() - 커널안에 존재하는 함수


## CPU mode 2가지
* User mode, Kenel mode

## Privileged instructions
* CPU가 반드시 커널모드에서만 실행가능한 기계어 명령어