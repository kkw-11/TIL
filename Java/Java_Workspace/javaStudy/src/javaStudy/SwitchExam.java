package javaStudy;

public class SwitchExam {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//switch, case, default, break
		
		int value = 1;
		
		switch(value) {
			case 1:
				System.out.println("1");
				break;
			case 2:
				System.out.println("2");
				break;
			case 3:
				System.out.println("3");
				break;
			default:
				System.out.println("others");
		
		}
		
		String str = "A";
		switch(str) {
		case "A":
			System.out.println("A");
			break;
		case "B":
			System.out.println("B");
		default:
			System.out.println("c");
		}
		// month���� ������ �� ������ ��� �ֽ��ϴ�.
		int month = 6;
        String season = "";
        // switch���� �̿��ؼ� season�� ������ � �������� ��Ÿ���� ��������.
        switch(month){
            case 12: case 1: case 2:
                season = "�ܿ�";
                break;
            case 3: case 4: case 5:
                season = "��";
                break;
            case 6: case 7: case 8:
                season = "����";
                break;
            case 9: case 10: case 11:
                season = "����";
                break;
            
        }
        

	        System.out.println("������ " + month + "���̰�, " + season + "�Դϴ�.");
	

				
		
	}

}
