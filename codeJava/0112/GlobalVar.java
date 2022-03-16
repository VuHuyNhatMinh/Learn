public class GlobalVar {
    int age;    // Instance/global
    // public void intAge() {
    public static void intAge() {
        int age = 15;   // Local Var
        System.out.println(age);
    }

    public static void main(String[] args) {
        intAge();
    }
}