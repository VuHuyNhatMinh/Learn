package Work;
import java.util.*;

public class Operators {
    public void oper() {
        System.out.print("Enter x = ");
        Scanner sc= new Scanner(System.in);
        int x = sc.nextInt();

        System.out.print("Enter y = ");
        int y = sc.nextInt();

        // Increment and decrement operators.
        System.out.println("This is Increment and decrement operators.");

        System.out.println("++x = " + (++x));
        x = x - 1;

        System.out.println("x++ = " + (x++));
        x = x - 1;

        System.out.println("--x = " + (--x));
        x = x + 1;

        System.out.println("x-- = " + (x--));
        x = x + 1;

        System.out.println("--------------------------------");

        // Bitwise Complement operator.
        System.out.println("This is Bitwise Complement operator.");
        System.out.println("~x = " + (~x));

        System.out.println("--------------------------------");

        // Arithmetic operator.
        System.out.println("This is Arithmetic operators.");

        System.out.println("Addition: x + y = " + (x + y));
        System.out.println("Subtraction: x - y = " + (x - y));
        System.out.println("Multiplication: x * y = " + (x * y));
        System.out.println("Division: x / y = " + (x / y));
        System.out.println("Modulo: x % y = " + (x % y));

        System.out.println("--------------------------------");

        // Relational operators.
        System.out.println("x == y: " + (x == y));
        System.out.println("x != y: " + (x != y));
        System.out.println("x < y: " + (x < y));
        System.out.println("x > y: " + (x > y));
        System.out.println("x <= y: " + (x <= y));
        System.out.println("x >= y: " + (x >= y));

        System.out.println("--------------------------------");

        // Bitwise operators.
        System.out.println("x & y = " + (x & y));
        System.out.println("x ^ y = " + (x ^ y));
        System.out.println("x | y = " + (x | y));
        System.out.println("x >> y = " + (x >> y));
        System.out.println("x << y: " + (x << y));
        System.out.println("x >>> y: " + (x >>> y));

        System.out.println("--------------------------------");

        // Conditional operator.
        System.out.println("x == y ? " + "Yes : " + "No = " + (x == y?"Yes":"No"));
    }

}
