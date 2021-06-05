package javaStudy;

import java.util.Scanner;

public class DowhileExam {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int value = 0;
		Scanner scan = new Scanner(System.in);
		do {
			//반복할 문장들
			value = scan.nextInt();
			System.out.println("Input value:"+value);
		}while(value !=10);
		System.out.println("whlie finish!");
	}

}
