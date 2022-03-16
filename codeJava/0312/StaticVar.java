public class StaticVar {
    static int age;     // instance/global
    public static void intAge() {
        age = 15;   // local var
        System.out.println(age);
    }

    public void intAge2() {
        age = 50;   // local var
        System.out.println(age);
    }

    public static void intAge3() {
        int age = 220;
        System.out.println(age);
    }

    public static void main(String[] args) {
        intAge();
        StaticVar var = new StaticVar();
        var.intAge2();
        intAge3();
        System.out.println(age);
    }
}