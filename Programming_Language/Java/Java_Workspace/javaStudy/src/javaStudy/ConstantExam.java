package javaStudy;

public class ConstantExam {
	public static void main(String[] args) {
		int i;
		i = 10;
		i = 5;
		final int J = 10; //����� �빮�ڷ�
//		J = 5; //��� ���� �Ұ���
		
		double circleArea;
		final double PI = 3.14159;
		
//		circleArea = 3*3*3.14159;
		circleArea = 3*3*PI;
		
		final int OIL_PRICE = 1390;
		
		int totalPrice = 50 * OIL_PRICE;
		System.out.println(circleArea);
		
	}
}
