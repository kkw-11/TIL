package javaStudy;

public class ArrayWithFor {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] iarray = new int[100];
		iarray[0] = 1;
		iarray[1] = 2;
		
		System.out.println(iarray.length);
		
		for(int i = 0; i<iarray.length;++i) {
			iarray[i] = i+1;
		}
		
		int total = 0;
		for(int j = 0; j<iarray.length;++j) {
			total += iarray[j];
			System.out.println(iarray[j]);
		}
		System.out.println(total);
		
	}

}
