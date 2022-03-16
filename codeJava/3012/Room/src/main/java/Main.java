package Work;

public class Main {
    public static void main(String[] args) {
        System.out.println("-------------1st HW-------------");
        Operators operator = new Operators();
        operator.oper();

        System.out.println("-------------2nd HW-------------");
        Control control = new Control();
        control.con();

        System.out.println("-------------3th HW-------------");
        Arrays array = new Arrays();
        array.arr();

        System.out.println("-------------4th HW-------------");
        System.out.println("Command line arguments");
        int argc = args.length;
        System.out.println("Argument count: " + argc);
        System.out.println("Arguments");
        for (int i = 0 ; i < argc ; i = i + 1) {
            System.out.printf("%d: %s\n", i, args[i]);
        }

        System.out.println("-------------5th HW-------------");
        // Room instance
        Room room = new Room();
        room.getData();

        System.out.println("-------------6th HW-------------");
        // SimpleObject instance;
        SimpleObject object = new SimpleObject("This is Constructor");

        // 'this' operator
        object.setMessage("Test");
        System.out.println("Try 'this' operator: " + object.getMessage());
    }
}
