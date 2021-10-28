package javaStudy;

public class OperatorExam5 {
	
	public static void main(String[] args) {
		boolean b1 = true;
		boolean b2 = false;
		boolean b3 = true;
		
		System.out.println(b1 && b2);
		System.out.println(b1 && b3);
		System.out.println(b1 || b2);
		System.out.println(b1 || b3);
		System.out.println(b2 || b2);
		
		int score = 8;
		if(score<= 100 &&score>=70) {
			System.out.println("Success");
		}else {
			System.out.println("Fail");
		}
		
		System.out.println(b1 ^ b3);
		System.out.println(b1 ^ b2);
		System.out.println(!b1);
	}
		
}
