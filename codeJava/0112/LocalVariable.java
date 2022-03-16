public class LocalVariale {
    private static void intAge() {
        int age = 15;   // local
        System.out.println(age);
    }

    public static void main(String[] args) {
        int year = 1990;
        if (year > 0) {
            int age = 2021 - year;   // local in if;
            System.out.println(age);
        }

        intAge();
    }
}