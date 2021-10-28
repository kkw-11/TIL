package javaStudy;

public class whileExam {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
//		int i = 0;
//		
//		while(i<10) {
//			System.out.println(i++);
//		}
		
		int total = 0;
		int i = 1;
		while(i<=100) {
			total += i;
			++i;
		}
		System.out.println(total);
		while(true) {
			System.out.println("Hello");
		}
	}

}
