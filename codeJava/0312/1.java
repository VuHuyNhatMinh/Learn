public class GlobalVar {
    int age;    // instance/global
    public void intAge() {
        age = 15;   // local var
        System.out.println(age);
    }

    public static void main(String[] args) {
        GlobalVar var = new GlobalVar();
        var.intAge();
    }
}