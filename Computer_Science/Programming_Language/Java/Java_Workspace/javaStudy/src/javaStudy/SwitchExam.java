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
		// month에는 오늘이 몇 월인지 들어 있습니다.
		int month = 6;
        String season = "";
        // switch문을 이용해서 season이 오늘은 어떤 계절인지 나타내게 만들어보세요.
        switch(month){
            case 12: case 1: case 2:
                season = "겨울";
                break;
            case 3: case 4: case 5:
                season = "봄";
                break;
            case 6: case 7: case 8:
                season = "여름";
                break;
            case 9: case 10: case 11:
                season = "가을";
                break;
            
        }
        

	        System.out.println("지금은 " + month + "월이고, " + season + "입니다.");
	

				
		
	}

}
