package Work;
import java.util.Scanner;

public class Control {
    public void con() {
        System.out.print("Enter x = ");
        Scanner sc= new Scanner(System.in);
        int x = sc.nextInt();

        System.out.print("Enter y = ");
        int y = sc.nextInt();

        // If statement.
        System.out.printf("If statement: x > y? Ans: ");
        if (x > y) {
            System.out.println("Yes");
        }
        else {
            System.out.println("No");
        }

        // Switch statement
        System.out.println("Switch statement");
        System.out.printf("Choose from 1 to 3: ");
        int c = sc.nextInt();

        switch (c) {
            case 1:
                System.out.println("You chose 1.");
                break;
            case 2:
                System.out.println("You chose 2.");
                break;
            case 3:
                System.out.println("You chose 3.");
                break;
            default:
                System.out.println("Out of range.");
        }

        // For loop.
        for (int i = 0 ; i < x ; i = i + 1) {
            System.out.println("This is boring!");
        }

        // While statement.
        int i = 0;
        while (i < x) {
            System.out.println("This is useless!");
            i = i + 1;
        }

        // Do statement.
        i = 0;
        do {
            System.out.println("This is boring!");
            i = i + 1;
        } while (i < x);
    }
}
