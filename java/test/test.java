import java.util.Scanner;


public class test {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int [] nums= new int [10];
		for (int i=0; i<1; i++) {
			nums[i]=scanner.nextInt();
		}
		for (int i=0; i<1; i++) {
			if (nums[i] %3 ==0) {
				System.out.print (nums[i]+ ' ');
			}
		}
	}

}
