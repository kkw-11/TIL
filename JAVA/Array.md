## Array
* Array(배열)은 같은 타입의 여러 변수를 하나의 묶음으로 다루는 것

## 배열의 선언과 생성
* 배열을 선언하는 방법은 원하는 타입의 변수를 선언하고 변수 또는 타입에 배열임을 의미하는 대괄호\[]를 붙이면 된다. 대괄호[]는 타입 뒤에 붙여도 되고 변수이름 뒤에 붙여도 된다. 하지만 Java 에서는 타입에 붙이는 쪽이 많다. 대괄호가 변수이름의 일부라기보다 타입의 일부라고 보는 경우가 많기 때문이다.
![image](https://user-images.githubusercontent.com/76929823/120873910-17a4fe80-c5df-11eb-88fe-a6592baee4b0.png)
  ### 배열의 생성
  
  ```
  int[] score;  //배열 선언(배열을 다루기 위한 참조변수 선언)
  score = new int[5]; //배열을 생성(실제 메모리 저장공간 생성)
  ```
  
  ### int[] score;
  
  * int형 배열 참조변수 score를 선언한다. 데이터를 저장할 수 있는 공간은 아직 마련되지 않았다.
    
      ![image](https://user-images.githubusercontent.com/76929823/120874047-b7fb2300-c5df-11eb-936f-cf2039caf918.png)
  
  ### score = new int\[5];
  
  * 연산자 'new'에 의해서 메모리의 빈 공간에 5개의 int형 데이터를 저장할 수 있는 공간이 마련된다.
   ![image](https://user-images.githubusercontent.com/76929823/120874099-f09afc80-c5df-11eb-8af1-19a40fcfe18d.png)
  
  * 그리고 각 배열 요소는 자동적으로 int의 기본값(default)인 0으로 초기화 된다.
   ![image](https://user-images.githubusercontent.com/76929823/120874129-158f6f80-c5e0-11eb-8953-235d3440a522.png)
  
  * 끝으로 대입 연산자'+'에 의해 배열의 주소가 int형 배열 참조변수 score에 저장된다.
   ![image](https://user-images.githubusercontent.com/76929823/120874151-31931100-c5e0-11eb-849d-c355b18ce86a.png)
  
  * 이제 참조변수 score를 통해서 생성된 배열에 값을 저아하거나 읽어 올 수 있다. 이 배열은 '길이가 5인 int배열'이며, 참조변수의 이름을 따서 '배열 score'라고 부르면 된다.





