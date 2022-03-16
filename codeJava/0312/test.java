class Test {
    public static void main(String[] args) {
        int i = 2;
        int j = 3;
        int a;
        a = i+++j;
        System.out.println(a);
        System.out.println(i);
        System.out.println(j);

        i = 2;
        j = 3;
        a = i + ++j;
        System.out.println(a);
        System.out.println(i);
        System.out.println(j);

        i = 2;
        j = 3;
        a = i++ + j;
        System.out.println(a);
        System.out.println(i);
        System.out.println(j);
    }
}