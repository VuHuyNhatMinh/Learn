package Model;


import java.util.Date;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Students student = new Students();
        Scanner sc = new Scanner(System.in);

        String name;
        name = sc.nextLine();
        student.setFullName(name);
        System.out.printf("name: %s\n", student.getFullName());

        Date date;
        date = Date(sc.nextLine());
    }
}
